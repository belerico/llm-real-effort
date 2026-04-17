/*
 * Per-puzzle timeout. Include AFTER the game-specific JS.
 * Reads js_vars.params.puzzle_timeout (seconds). 0 or absent = disabled.
 *
 * When the timer fires:
 *   1. Freezes the UI and sends {type:'timeout'} to the server
 *   2. Server marks the puzzle as TIMEOUT, returns feedback with timed_out=true
 *   3. JS auto-advances to the next puzzle immediately (no user interaction)
 */
(function () {
    if (typeof liveSend === 'undefined') return;

    var _timer = null;
    var _movingForward = false;
    var _serverIter = 0;
    var _origNewPuzzle = newPuzzle;
    var _origLiveRecv = liveRecv;
    var _origMoveForward = moveForward;

    function _startTimer() {
        _clearTimer();
        var timeout = (js_vars.params || {}).puzzle_timeout || 0;
        if (timeout > 0) {
            _timer = setTimeout(function () {
                _timer = null;
                setFrozen(true);
                lockInput();
                liveSend({type: 'timeout'});
            }, timeout * 1000);
        }
    }

    function _clearTimer() {
        if (_timer) { clearTimeout(_timer); _timer = null; }
    }

    // Wrap newPuzzle: reset state, run original, start timer
    newPuzzle = function (data) {
        _clearTimer();
        _movingForward = false;
        setFrozen(false);
        _origNewPuzzle(data);
        _startTimer();
    };

    // Wrap moveForward: guard against double-move
    moveForward = function (wait) {
        if (_movingForward) return;
        _movingForward = true;
        _origMoveForward(wait);
    };

    // Wrap liveRecv: clear timer on feedback, auto-advance on timeout
    liveRecv = function (message) {
        if (message.type === 'feedback') _clearTimer();
        if ('progress' in message) _serverIter = message.progress.iteration;

        // Timeout feedback: skip puzzle_delay, advance immediately
        if (message.type === 'feedback' && message.timed_out) {
            showFeedback(message);
            if ('progress' in message) showProgress(message.progress);
            moveForward(0);
            return;
        }

        _origLiveRecv(message);
    };

    // Override submitAnswer: attach iteration for stale-answer protection
    submitAnswer = function () {
        if (isFrozen || input.value === "") return;
        lockInput();
        resetFeedback();
        liveSend({type: 'answer', answer: input.value, iteration: _serverIter});
    };
})();
