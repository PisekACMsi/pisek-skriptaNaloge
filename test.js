var before = ["red", "brown", "green"]
var after = ["green", "brown"]
function beforeAfter(before, after){
    var dodani = []
    var odvzeti = []
  for (var a of after){
    if (!before.includes(a)){
        dodani.push(a)
    }
  }

  for (var b of before){
    if (!after.includes(b)){
        odvzeti.push(b)
    }
  }
  return [dodani, odvzeti]
}


var index = before.indexOf("brown");
if (index !== -1) {
    before.splice(index, 1);
}
console.log(before)