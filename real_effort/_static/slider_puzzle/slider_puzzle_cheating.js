let cheat_btn = document.getElementById('cheat-btn');
if (cheat_btn) {
    cheat_btn.onclick = function() {
        liveSend({'type': 'cheat'});
    }
}

function cheat(solution) {
    // Auto-solve: send each move with a delay
    let moves = solution.split(' ').map(Number);
    let i = 0;
    function doMove() {
        if (i < moves.length) {
            liveSend({type: 'move', tile: moves[i]});
            i++;
            setTimeout(doMove, 200);
        }
    }
    doMove();
}
