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

  $('#robot-single-blocks-dropdown').on('changed.bs.select', function (e, clickedIndex, isSelected, previousValue) {
    if (clickedIndex === 0 && isSelected) {
      $('#robot-single-blocks-dropdown').selectpicker('selectAll');
    } else if (clickedIndex === 0 && !isSelected) {
      $('#robot-single-blocks-dropdown').selectpicker('deselectAll');
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

function refreshScene(path) {
          // Perform your logic to generate the updated content

  if (path == "addRobot"){
    var dict = {
      "coordRowR": document.getElementById('robot-coord-y').value,
      "coordColR": document.getElementById('robot-coord-x').value,
      "itemImageR": document.getElementById('robot-image').value
    }
  }
  else if (path == "defaultItem"){
    var dict = {
      "defaultItemCategory": document.getElementById('default-item-category').value,
      "defaultItemImage": document.getElementById('default-item-image').value
    }
  }
  else if (path == "defaultNumber"){
    var dict = {
      "defaultItemNumber": document.getElementById('default-item-number').value,
    }
  }
  else if (path == "defaultColor"){
    var dict = {
      "defaultItemColor": document.getElementById('default-item-color').value,
    
    }
  }
  else if (path == "defaultButton"){
    var dict = {
      "defaultButtonImageOn": document.getElementById('default-button-on-image').value,
      "defaultButtonImageOff": document.getElementById('default-button-off-image').value,
    }
  }
  else if (path == "customObject"){
    var categoryOptions = document.getElementById('custom-item-category').selectedOptions;
    var selectedCategories = []
    for (var i = 0; i < categoryOptions.length; i++) {
      var option = categoryOptions[i];
      selectedCategories.push(option.value)
    }
    var imageOptions = document.getElementById('custom-item-image').selectedOptions;
    var selectedImages= []
    for (var i = 0; i < imageOptions.length; i++) {
      var option = imageOptions[i];
      selectedImages.push(option.value + ".png")
    }
    var colorOptions = document.getElementById('custom-item-color').selectedOptions;
    var selectedColors = []
    for (var i = 0; i < colorOptions.length; i++) {
      var option = colorOptions[i];
      selectedColors.push(option.value)
    }
    var buttonName = document.getElementById('custom-button-id').value;
    var buttonId = buttonName.substr(buttonName.indexOf("_")+1, buttonName.length)
    var dict = {
      "itemName": document.getElementById('custom-item-name').value,
      "itemCategory": JSON.stringify(selectedCategories),
      "itemImage": JSON.stringify(selectedImages),
      "itemValue": document.getElementById('custom-item-value').value,
      "itemZOrder": document.getElementById('custom-item-z-order').value,
      "buttonId": buttonId,
      "itemColor": JSON.stringify(selectedColors),
    }
  }
  else if (path == "addToMatrix"){
    var dict = {
      "itemName": document.getElementById('added-item-to-matrix').value,
      "itemRow": document.getElementById('add-coord-row').value,
      "itemCol": document.getElementById('add-coord-col').value,
    }
  }
  else if (path == "removeFromMatrix"){
    var dict = {
      "itemName": document.getElementById('added-item-to-matrix').value,
      "itemRow": document.getElementById('add-coord-row').value,
      "itemCol": document.getElementById('add-coord-col').value,
    }
  }
  else if (path == "removeItem"){
    var dict = {
      "delName": document.getElementById('remove-item-name').value,
    }
  }

  $.ajax({
  url: "\\" + path,  // Replace with the appropriate server route
  type: 'POST',
  data: dict,
  success: function(response) {
  },
});

$.ajax({
  url: "/updateItemTypes",  // Replace with the appropriate server route
  type: 'GET',
  data: {},
  success: function(response) {
    $('#scene').html(response);
  },
});

$.ajax({
  url: "/updateItemTypeOptions",  // Replace with the appropriate server route
  type: 'POST',
  data: {},
  success: function(response) {
    selected1 = document.getElementById('added-item-to-matrix').value;
    r1 = response.replace("<option>" + selected1, '<option selected="selected">'+ selected1);
    $('#added-item-to-matrix').html(r1);
    $('#remove-item-name').html(r1);
    
    selected2 = document.getElementById('coincide-label-A').value;

    res = '<option></option><br>' + response
    r2 = res.replace("<option>" + selected2, '<option selected="selected">'+ selected2);
    $('#coincide-label-A').html(r2);
    
    selected3 = document.getElementById('coincide-label-B').value;
    r3 = res.replace("<option>" + selected3, '<option selected="selected">'+ selected3);
    $('#coincide-label-B').html(r3);
  },
});

$.ajax({
  url: "/updateButtons",  // Replace with the appropriate server route
  type: 'GET',
  data: {},
  success: function(response) {
    $('#custom-button-id').html(r1);
  },
});

  // osvezi('pisek-iframe');
  }

  
function updateLangugaeStrings() {
  var idLS = document.getElementById('id-LS').value;
  var textLS = document.getElementById('text-LS').value;
  $.ajax({
    type: 'POST', // or 'GET' depending on your server-side implementation
    url: '/ls', // Replace with the actual route on your Bottle server
    data: {
      "idLS":idLS,
      "textLS": textLS
    },
    success: function(response) {
      console.log('Request successful');
      $('#select-LS').html(response);
    },
    error: function(xhr, status, error) {
      // Handle errors
      console.error('Error:', error);
    }
  });
};

function createNewCategory(){
  var category = document.getElementById('custom-category-name').value;
  $.ajax({
    type: 'POST', // or 'GET' depending on your server-side implementation
    url: '/createNewCategory', // Replace with the actual route on your Bottle server
    data: {
      "category":category,
    },
    success: function(response) {
      console.log('Request successful');
      $('#custom-item-category').html(response);
    },
    error: function(xhr, status, error) {
      // Handle errors
      console.error('Error:', error);
    }
  });
}

function resetAll(){
  $.ajax({
    type: 'POST', // or 'GET' depending on your server-side implementation
    url: '/resetFile', // Replace with the actual route on your Bottle server
    data: {
    },
    success: function(response) {
    },
    error: function(xhr, status, error) {
      // Handle errors
      console.error('Error:', error);
    }
  });
  location.reload();
}
  
  
  
  
  