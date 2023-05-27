var newURL_polje = "";
var newURL_junak = "";
$(document).ready(function () {
  $("#junak").change(function () {
    var value = $("#junak option:selected");
    newURL_junak = "../static/img/characters/" + value.text().split(' ').join('_') + ".png";
    $("#slika1").attr("src", newURL_junak);
  });
});

$(document).ready(function () {
  $("#polje").change(function () {
    var value = $("#polje option:selected");
    newURL_polje = "../static/img/tiles/" + value.text().split(' ').join('_') + ".png";
    $("#slika2").attr("src", newURL_polje);
    $('.grid img').attr('src', newURL_polje);
  });
});
// function that builds a grid in the "container"
function createGrid(x, y) {
  for (var rows = 0; rows < y; rows++) {
    for (var columns = 0; columns < x; columns++) {
      $("#container").append("<div " + "id=" + rows + "." + columns + " class='grid'><img src = ''></div>");
    };
  };
  $(".grid").width(480 / x);
  $(".grid").height(480 / x);
  $('.grid img').css({ 'height': 480 / x, 'width': 480 / x });
  $('.grid img').attr('src', newURL_polje);
  var vrstica_junak = $("#vrstica-junak").val();
  var stolpec_junak = $("#stolpec-junak").val();

  // Preverimo ali ima junak vnešene parametre za položaj
  if (!isNaN(parseFloat(stolpec_junak)) && isFinite(stolpec_junak) && parseFloat(vrstica_junak) && isFinite(vrstica_junak)) {

  } else {
    console.log("Input value is not a number");
  }
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

//če kliknemo na block-includeAll bomo disablali vse ostale inpute
$(document).ready(function () {
  $('#blocks-includeAll').change(function () {
    if ($(this).is(':checked')) {
      // Disable all other checkboxes
      $('input[type="checkbox"]').not(this).prop('disabled', true);
    } else {
      // Enable all checkboxes
      $('input[type="checkbox"]').not(this).prop('disabled', false);
    }
  });
});

//izberimo vse oz. ne
$(document).ready(function() {
  $('#blocks-dropdown').on('changed.bs.select', function(e, clickedIndex, isSelected, previousValue) {
    if (clickedIndex === 0 && isSelected) {
      $('#blocks-dropdown').selectpicker('selectAll');
    } else if (clickedIndex === 0 && !isSelected) {
      $('#blocks-dropdown').selectpicker('deselectAll');
    }
  });

  $('#robot-blocks-dropdown').on('changed.bs.select', function(e, clickedIndex, isSelected, previousValue) {
    if (clickedIndex === 0 && isSelected) {
      $('#robot-blocks-dropdown').selectpicker('selectAll');
    } else if (clickedIndex === 0 && !isSelected) {
      $('#robot-blocks-dropdown').selectpicker('deselectAll');
    }
  });
});