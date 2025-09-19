const rps = (p1, p2) => {
  if (p1 === p2) return 'Draw!';

  const beats = {
    scissors: 'paper',
    paper: 'rock',
    rock: 'scissors',
  };

  if (beats[p1] === p2) return 'Player 1 won!';
  return 'Player 2 won!';
};
