/*
Sliding tile puzzle. Renders an interactive grid; player clicks tiles
adjacent to the empty space to slide them. Uses the same live_method
WebSocket protocol as other games.
*/

let isFrozen = false;
let currentState = null;
let puzzleSize = 3;
let moveCount = 0;

let grid = document.getElementById('puzzle-grid');
let warn = document.getElementById('warning-txt');
let movesTxt = document.getElementById('moves-txt');
let fields = {
    iter: document.getElementById('iter-txt'),
    solved: document.getElementById('solved-txt'),
    failed: document.getElementById('failed-txt'),
}

// Read grid size from data attribute
puzzleSize = parseInt(grid.dataset.size) || 3;

document.addEventListener("DOMContentLoaded", (event) => {
    liveSend({type: 'load'});
});

function liveRecv(message) {
    switch(message.type) {

        case 'status':
            if (message.puzzle) {
                newPuzzle(message.puzzle);
            } else if (message.progress.iteration === 0) {
                liveSend({type: 'next'});
            } else if (message.iterations_left === 0) {
                document.getElementById("form").submit();
            }
            break;

        case 'puzzle':
            newPuzzle(message.puzzle);
            break;

        case 'moved':
            // Update board after a valid move
            renderBoard(message.puzzle.state);
            break;

        case 'solved':
            renderBoard(message.puzzle.state);
            showSolved();
            moveForward(js_vars.params.puzzle_delay);
            break;

        case 'invalid_move':
            // Tile click was invalid; just ignore
            break;

        case 'feedback':
            showFeedback(message);
            if (message.is_correct === false && message.retries_left > 0) {
                tempFreeze(js_vars.params.retry_delay);
            } else {
                moveForward(js_vars.params.puzzle_delay);
            }
            break;

        case 'solution':
            cheat(message.solution);
            break;
    }

    if ('progress' in message) {
        showProgress(message.progress);
    }
}

function newPuzzle(data) {
    currentState = data.state;
    puzzleSize = data.size || puzzleSize;
    moveCount = 0;
    movesTxt.textContent = 'Moves: 0';
    renderBoard(currentState);
    resetFeedback();
    setFrozen(false);
}

function renderBoard(state) {
    currentState = state;
    grid.innerHTML = '';
    grid.style.gridTemplateColumns = `repeat(${puzzleSize}, 1fr)`;

    for (let i = 0; i < state.length; i++) {
        let tile = document.createElement('div');
        let val = state[i];

        if (val === 0) {
            tile.className = 'puzzle-tile puzzle-empty';
        } else {
            tile.className = 'puzzle-tile';
            tile.textContent = val;
            tile.dataset.tile = val;
            tile.addEventListener('click', function () {
                onTileClick(val);
            });
        }
        grid.appendChild(tile);
    }
}

function onTileClick(tile) {
    if (isFrozen) return;
    setFrozen(true);
    liveSend({type: 'move', tile: tile});
    // Unfreeze after a short delay to prevent rapid clicks
    setTimeout(function () { setFrozen(false); }, 150);
    moveCount++;
    movesTxt.textContent = 'Moves: ' + moveCount;
}

function showSolved() {
    // Briefly highlight the grid
    grid.classList.add('puzzle-solved');
    setTimeout(function () {
        grid.classList.remove('puzzle-solved');
    }, 1000);
}

function resetPuzzle() {
    grid.innerHTML = '';
}

// Compatibility stubs for puzzle_timer.js
let input = { disabled: false, value: '', classList: { remove: function(){}, add: function(){} } };

function resetInput() {}
function lockInput() { setFrozen(true); }
function enableInput() { setFrozen(false); }

function submitAnswer() {
    // Not used in interactive mode; stub for puzzle_timer override
}

function resetFeedback() {
    warn.textContent = '';
    grid.classList.remove('puzzle-solved');
}

function showFeedback(data) {
    if (data.is_correct) {
        showSolved();
    } else if (data.timed_out) {
        warn.textContent = 'Time is up!';
    }
}

function moveForward(wait) {
    window.setTimeout(gotoNext, wait * 1000);
}

function gotoNext() {
    resetPuzzle();
    resetFeedback();
    liveSend({type: 'next'});
}

function showProgress(data) {
    fields.iter.textContent = data.iteration;
    fields.solved.textContent = data.num_correct;
    fields.failed.textContent = data.num_incorrect;
}

function waitMsg(seconds) {
    warn.textContent = `Wait ${Math.round(seconds)} seconds before trying again`;
}

function setFrozen(val) {
    isFrozen = val;
}

function tempFreeze(countdown) {
    setFrozen(true);
    waitMsg(countdown);
    let timer = window.setInterval(function() {
        countdown -= 1;
        if (countdown > 0) {
            waitMsg(countdown);
        } else {
            setFrozen(false);
            warn.textContent = "";
            clearInterval(timer);
        }
    }, 1000);
}
