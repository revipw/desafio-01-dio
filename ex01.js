function calculate(wins, loses){
    return (wins-loses);
}
let LP = calculate(80, 35);
let elo;
if(LP <= 10){
    elo = 'Ferro'
}else if(LP >= 11 && LP <= 20){
    elo =  'Bronze'
}else if(LP >= 21 && LP <= 50){
   elo =  'Prata'
}else if(LP >= 51 && LP <= 80){
    elo =  'Ouro'
}else if(LP >= 81 && LP <= 90){
   elo =  'Diamante'
}else if(LP >= 91 && LP <= 100){
   elo =  'Lendário'
}else{
   elo =  'Imortal'
}

console.log("The Hero has " + LP + " LP and it's on level " + elo +"!");
 