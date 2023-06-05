//pot do items
var newURL_polje = "";
var newURL_junak = "";
var newURL_predmet = "";

//velikost slik na gridu
var velikost_x = 0;
var velikost_y = 0;
//funkcija, ki prikaže sliko za glavnega junaka
$(document).ready(function () {
  $("#junak").change(function () {
    var value = $("#junak option:selected");
    newURL_junak = "../static/img/characters/" + value.text().split(' ').join('_') + ".png";
    $("#slika1").attr("src", newURL_junak);
  });
});

//funkcija, ki prikaže sliko za polje in jo izriše na gridu
$(document).ready(function () {
  $("#polje").change(function () {
    var value = $("#polje option:selected");
    newURL_polje = "../static/img/tiles/" + value.text().split(' ').join('_') + ".png";
    $("#slika2").attr("src", newURL_polje);
  });
});

//funkcija, ki prikaže sliko za predmet
$(document).ready(function () {
  $("#item").change(function () {
    var value = $("#item option:selected");
    newURL_predmet = "../static/img/objects/" + value.text().split(' ').join('_') + ".png";
    $("#slika3").attr("src", newURL_predmet);
  });
});

// function that builds a grid in the "container"
function createGrid(x, y) {
  for (var rows = 1; rows <= y; rows++) {
    for (var columns = 1; columns <= x; columns++) {
      $("#container").append("<div " + "id=" + rows + "." + columns + " class='grid'><img src = '' onerror='this.onerror=null; this.remove();'></div>");
    };
  };
  $(".grid").width(480 / x);
  $(".grid").height(480 / x);
  $('.grid img').css({ 'height': 480 / x, 'width': 480 / x, 'position': 'absolute' });
  $('.grid img').attr('src', newURL_polje);
  var vrstica_junak = $("#vrstica-junak").val();
  var stolpec_junak = $("#stolpec-junak").val();
  velikost_x = 480 / x;
  velikost_y = 480 / x;
};

// function that clears the grid
function clearGrid() {
  $(".grid").remove();
};

// function that prompts the user to select the number of boxes in a new grid
// the function then also creates that new grid
function refreshGrid() {
  var columns = document.getElementById("polje-stolpec").value;
  var rows = document.getElementById("polje-vrstica").value;
  clearGrid();
  createGrid(parseInt(columns), parseInt(rows));
};
// create a 16x16 grid when the page loads
// creates a hover effect that changes the color of a square to black when the mouse passes over it, leaving a (pixel) trail through the grid
// allows the click of a button to prompt the user to create a new grid
$(document).ready(function () {
  createGrid(2, 2);
});


//izberimo vse oz. ne
$(document).ready(function () {
  $('#blocks-dropdown').on('changed.bs.select', function (e, clickedIndex, isSelected, previousValue) {
    if (clickedIndex === 0 && isSelected) {
      $('#blocks-dropdown').selectpicker('selectAll');
    } else if (clickedIndex === 0 && !isSelected) {
      $('#blocks-dropdown').selectpicker('deselectAll');
    }
  });

  $('#robot-blocks-dropdown').on('changed.bs.select', function (e, clickedIndex, isSelected, previousValue) {
    if (clickedIndex === 0 && isSelected) {
      $('#robot-blocks-dropdown').selectpicker('selectAll');
    } else if (clickedIndex === 0 && !isSelected) {
      $('#robot-blocks-dropdown').selectpicker('deselectAll');
    }
  });
});

//funkcija doda sliko na neko mesto na gridu
function izrisi_objekt(tip) {
  if (tip == 'objekt') {
    var vrstica_objekt = $("#stolpec-objekt-vrstica").val();
    var stolpec_objekt = $("#stolpec-objekt-stolpec").val();
    var newImageElement = $("<img>").attr("src", newURL_predmet);
  }
  else {
    var vrstica_objekt = $("#povrsina-vrstica").val();
    var stolpec_objekt = $("#povrsina-stolpec").val();
    var newImageElement = $("<img>").attr("src", newURL_polje);
  }
  newImageElement.css({
    "height": velikost_x,
    "width": velikost_y,
    "position": 'absolute'
  });
  $("#" + vrstica_objekt + "\\." + stolpec_objekt).append(newImageElement);
}

//funkcija izbrise zadnji objekt iz polja
function izbrisi_zadnji_objekt() {
  var vrstica_objekt = $("#izbrisi-objekt-vrstica").val();
  var stolpec_objekt = $("#izbrisi-objekt-stolpec").val();

  $("#" + vrstica_objekt + "\\." + stolpec_objekt).find("img").last().remove();
}

//funkcija osveži iframe
function osvezi(id) {
  document.getElementById(id).contentWindow.location.reload();
}

//osveži iteme
function refreshDiv(divId) {
  $('#' + divId).load('http://localhost/index.html #' + divId);
}