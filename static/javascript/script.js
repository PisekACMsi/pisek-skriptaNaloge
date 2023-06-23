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
  $('#blocks-category-dropdown').on('changed.bs.select', function (e, clickedIndex, isSelected, previousValue) {
    if (clickedIndex === 0 && isSelected) {
      $('#blocks-category-dropdown').selectpicker('selectAll');
    } else if (clickedIndex === 0 && !isSelected) {
      $('#blocks-category-dropdown').selectpicker('deselectAll');
    }
  });

  $('#blocks-robot-dropdown').on('changed.bs.select', function (e, clickedIndex, isSelected, previousValue) {
    if (clickedIndex === 0 && isSelected) {
      $('#blocks-robot-dropdown').selectpicker('selectAll');
    } else if (clickedIndex === 0 && !isSelected) {
      $('#blocks-robot-dropdown').selectpicker('deselectAll');
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

// var orderOfSelectedCategories = [];
// $(document).ready(function() {
//   $('#custom-item-category').selectpicker();

//   $('#custom-item-category').on('changed.bs.select', function(e) {
//     var selectedOptions = $(this).val();
//     if (selectedOptions == null){
//       orderOfSelectedCategories = []
//     }
//     else{
//       for(var del=0; del < orderOfSelectedCategories.length; del++){
//         if (! selectedOptions.includes(orderOfSelectedCategories[del])) orderOfSelectedCategories.splice(del, 1);

//       }
//       for(var add=0; add < selectedOptions.length; add++){
//         console.log(add)
//         if (! orderOfSelectedCategories.includes(selectedOptions[add])) orderOfSelectedCategories.push(selectedOptions[add]);

//       }
//   }
//   });
// });

// var orderOfSelectedImages= [];
// var prejsnjeStanje = new Set();
// $(document).ready(function() {
//   $('#custom-item-image').selectpicker();

//   $('#custom-item-image').on('changed.bs.select', function(e) {
//     var novoStanje = new Set($(this).val());
//     if (novoStanje == null){
//       orderOfSelectedImages = []
//     }
//     else{
//       [add] = new Set([...novoStanje].filter(element => !prejsnjeStanje.has(element)));
//       [dell] = new Set([...prejsnjeStanje].filter(element => !novoStanje.has(element)));
//       prejsnjeStanje = novoStanje
//       console.log("add " + add)
//       console.log("del " + dell)
//       if (add !== undefined) orderOfSelectedImages.push((add.includes("User") ? "objectsUser/" : "objects/") + add.replace(" ", "_").replace("User","") + (add ? '.png' : ''));
//       index = orderOfSelectedImages.indexOf(dell);
      
//       if(index>-1) orderOfSelectedImages.splice(index, 1);
//   }
//   console.log(orderOfSelectedImages);
//   });
// });

// var orderOfSelectedColors = [];
// $(document).ready(function() {
//   $('#custom-item-color').selectpicker();

//   $('#custom-item-color').on('changed.bs.select', function(e) {
//     var selectedOptions = $(this).val();
//     if (selectedOptions == null){
//       orderOfSelectedColors = []
//     }
//     else{
//       for (var colorIn of orderOfSelectedColors){
//         if (!selectedOptions.includes(colorIn)){
//           var index = orderOfSelectedColors.indexOf(colorIn);
//           if (index > -1) { // only splice array when item is found
//             orderOfSelectedColors.splice(index, 1); // 2nd parameter means remove one item only
//           }
//         }
//       }
//       for (var colorIn of selectedOptions){
//         if (!orderOfSelectedColors.includes(colorIn)){
//           orderOfSelectedColors.push(colorIn);
//         }
//       }
      
//       console.log(orderOfSelectedColors);
//   }
//   });
// });



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

function refreshText(){
  var dict = {
    "title": document.getElementById('exercise-title').value,
    "text1": document.getElementById('exercise-text').value,
    "text2": document.getElementById('exercise-text-2').value,
  }
  $.ajax({
    url: "/refreshText",  // ReplaceAll with the appropriate server route
    type: 'POST',
    data: dict,
    success: function(response) {
    },
  })

}


function refreshScene(path) {
          // Perform your logic to generate the updated content

  if (path == "addRobot"){
    var dict = {
      "itemImageR": ((image) => {return "characters" + (image.includes("User") ? "User/" : "/") + image.replace("User", "").replace(" ", "_") + (image ? ".png" : "");})(document.getElementById('robot-image').value),
    }
  }
  else if (path == "defaultItem"){
    let img = document.getElementById('default-item-image').value;
    var dict = {
      "defaultItemCategory": document.getElementById('default-item-category').value,
      "defaultItemImage": "objects" + (img.includes("User") ? "User/" : "/") + img.replaceAll(" ", "_").replace("User", "") + (img ? '.png' : '')
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
    img1 = document.getElementById('default-button-on-image').value;
    img2 = document.getElementById('default-button-off-image').value;
    var dict = {
      "defaultButtonImageOn": "buttons/" + img1.replaceAll(" ", "_") + (img1 ? '.png' : ''),
      "defaultButtonImageOff": "buttons/" + img2.replaceAll(" ", "_") + (img2 ? '.png' : ''),
    }
  }
  else if (path == "customObject"){
    var buttonName = document.getElementById('custom-button-id').value;
    var buttonId = buttonName.substr(buttonName.indexOf("_")+1, buttonName.length)
    buttonId = (buttonId ? buttonId:"0")
    console.log($('#custom-item-image').val());
    var dict = {
      "itemName": document.getElementById('custom-item-name').value,
      "itemCategory": JSON.stringify($('#custom-item-category').val()),
      "itemImage": JSON.stringify($('#custom-item-image').val()),
      "itemValue": document.getElementById('custom-item-value').value,
      "itemZOrder": document.getElementById('custom-item-z-order').value,
      "buttonId": buttonId,
      "itemColor": JSON.stringify($('#custom-item-color').val()),
    }
  }
  else if (path == "addToMatrix"){
    var dict = {
      "itemName": document.getElementById('added-item-to-matrix').value,
      "itemRow": document.getElementById('add-coord-row').value,
      "itemCol": document.getElementById('add-coord-col').value,
      // "activeExample": document.getElementById('test-example-option').value,
    }
  }
  else if (path == "removeFromMatrix"){
    var dict = {
      "itemName": document.getElementById('added-item-to-matrix').value,
      "itemRow": document.getElementById('add-coord-row').value,
      "itemCol": document.getElementById('add-coord-col').value,
      // "activeExample": document.getElementById('test-example-option').value,
    }
  }
  else if (path == "removeItem"){
    var dict = {
      "delName": document.getElementById('remove-item-name').value,
    }
  }

  $.ajax({
  url: "\\" + path,  // ReplaceAll with the appropriate server route
  type: 'POST',
  data: dict,
  success: function(response) {
  },
});

$.ajax({
  url: "/updateItemTypes",  // ReplaceAll with the appropriate server route
  type: 'GET',
  data: {},
  success: function(response) {
    $('#scene').html(response);
  },
});

$.ajax({
  url: "/updateItemTypeOptions",  // ReplaceAll with the appropriate server route
  type: 'POST',
  data: {},
  success: function(response) {
    selected1 = document.getElementById('added-item-to-matrix').value;
    r1 = response.replaceAll("<option>" + selected1, '<option selected="selected">'+ selected1)
    $('#added-item-to-matrix').html(r1);
    $('#remove-item-name').html(r1);
    
    selected2 = document.getElementById('coincide-label-A').value;

    r2 = (selected2 ? '<option value="" selected="selected">Ne preverjaj</option>':'<option value="">Ne preverjaj</option>')+response.replaceAll("<option>" + selected2, '<option selected="selected">'+ selected2);
    $('#coincide-label-A').html(r2);
    
    selected3 = document.getElementById('coincide-label-B').value;
    r3 = (selected3 ? '<option value="" selected="selected">Ne preverjaj</option>':'<option value="">Ne preverjaj</option>')+response.replaceAll("<option>" + selected3, '<option selected="selected">'+ selected3);
    $('#coincide-label-B').html(r3);
  },
});

$.ajax({
  url: "/updateButtons",  // ReplaceAll with the appropriate server route
  type: 'GET',
  data: {},
  success: function(response) {
    $('#custom-button-id').html(response);
  },
});

  // osvezi('pisek-iframe');
  }

function updateBlocks() {
  dict = {
    "categoryBlocks":JSON.stringify($('#blocks-category-dropdown').val()),
    "robotBlocks":JSON.stringify($('#blocks-robot-dropdown').val()),
    "singleBlocks":JSON.stringify($('#robot-single-blocks-dropdown').val()),
    "groupByCategory":document.getElementById('group-by-category').checked,
    "maxInstructions":document.getElementById('max-instructions').value,
  }

  $.ajax({
    type: 'POST', // or 'GET' depending on your server-side implementation
    url: '/updateBlocks', // ReplaceAll with the actual route on your Bottle server
    data: dict,
    success: function(response) {
    },
    error: function(xhr, status, error) {
      // Handle errors
      console.error('Error:', error);
    }
  });
  // osvezi('pisek-iframe');
};

function updateLanguageStrings() {
  var idLS = document.getElementById('select-LS').selectedIndex;
  var textLS = document.getElementById('text-LS').value;
  $.ajax({
    type: 'POST', // or 'GET' depending on your server-side implementation
    url: '/languageStrings', // ReplaceAll with the actual route on your Bottle server
    data: {
      "idLS":idLS,
      "textLS": textLS
    },
    success: function(response) {
      $('#select-LS').html(response);
    },
    error: function(xhr, status, error) {
      // Handle errors
      console.error('Error:', error);
    }
  });
  // osvezi('pisek-iframe');
};

function deleteStartingExample(){
  $.ajax({
    type: 'POST', // or 'GET' depending on your server-side implementation
    url: '/deleteStartingExample', // ReplaceAll with the actual route on your Bottle server
    data: {
    },
  });
}

function updateMatrixParameters() {
  backgroundImage = document.getElementById('background-image').value
  $.ajax({
    type: 'POST', // or 'GET' depending on your server-side implementation
    url: '/updateMatrixParameters', // ReplaceAll with the actual route on your Bottle server
    data: {
      "backgroundColor": document.getElementById('background-color').value,
      "borderColor": document.getElementById('border-color').value,
      "borderWidth": document.getElementById('border-width').value,
      "backgroundImage": ((image) => {return "tiles" + (image.includes("User") ? "User/" : "/") + image.replace("User", "").replace(" ", "_") + (image ? ".png" : "");})(document.getElementById('background-image').value),
      "showLabels": document.getElementById('show-labels').checked,
      "gravityOn": document.getElementById('gravity-on').checked,
      "activeExample": document.getElementById('active-example-update-matrix').value,
      "matrixLength": document.getElementById('update-matrix-length').value,
      "matrixHeight": document.getElementById('update-matrix-height').value,
    },
    success: function(response) {
      console.log('Request successful');
      $('#test-example-option').html(response);
    },
    error: function(xhr, status, error) {
      // Handle errors
      console.error('Error:', error);
    }
  });
  // osvezi('pisek-iframe');
};

function deleteExample(){
  $.ajax({
    type: 'POST', // or 'GET' depending on your server-side implementation
    url: '/deleteMatrixExamples', // ReplaceAll with the actual route on your Bottle server
    data: {
      "deleteExample": document.getElementById('test-example-option').value,
    },
    success: function(response) {
      console.log('Request successful');
      $('#test-example-option').html(response);
    },
    error: function(xhr, status, error) {
      // Handle errors
      console.error('Error:', error);
    }
  });
  // osvezi('pisek-iframe');
}

function createNewCategory(){
  var category = document.getElementById('custom-category-name').value;
  $.ajax({
    type: 'POST', // or 'GET' depending on your server-side implementation
    url: '/createNewCategory', // ReplaceAll with the actual route on your Bottle server
    data: {
      "category":category,
    },
    success: function(response) {
      console.log(response);
      $('#custom-item-category').html(response);
      $('#custom-item-category').selectpicker('refresh');
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
    url: '/resetFile', // ReplaceAll with the actual route on your Bottle server
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

function uploadImage(){
  var path = document.getElementById('upload-image');
  if(path=="Robot"){
    var fileInput = document.getElementById('upload-image-robot');
    path = "charactersUser";
  }
  else if(path=="Ozadje"){
    var fileInput = document.getElementById('upload-image-tile');
    path = "tilesUser";
  }
  else if(path=="Predmet"){
    var fileInput = document.getElementById('upload-image-object');
    path = "objectsUser";
  }
  
  // Create a new FormData object
  var formData = new FormData();

  formData.append('imageFile', fileInput.files[0]);
  formData.append("path", path + "User")
  $.ajax({
    type: 'POST',
    url: '/uploadImage', // Replace with the actual route on your Bottle server
    data: formData, // Pass the formData object directly
    processData: false, // Prevent jQuery from processing the data
    contentType: false, // Prevent jQuery from setting the content type
    success: function(response) {
      // Handle the success response from the server
      location.reload();
    },
    error: function(xhr, status, error) {
      // Handle errors
      console.error('Error:', error);
    }
  });
  // osvezi('pisek-iframe');
  
}

function uploadStartingExample(){
  
  var fileInput = document.getElementById('upload-starting-example-file');

  
  // Create a new FormData object
  var formData = new FormData();

  formData.append('imageFile', fileInput.files[0]);
  $.ajax({
    type: 'POST',
    url: '/uploadStartingExample', // Replace with the actual route on your Bottle server
    data: formData, // Pass the formData object directly
    processData: false, // Prevent jQuery from processing the data
    contentType: false, // Prevent jQuery from setting the content type
    success: function(response) {
      // Handle the success response from the server
      location.reload();
    },
    error: function(xhr, status, error) {
      // Handle errors
      console.error('Error:', error);
    }
  });
  // osvezi('pisek-iframe');
  
}

function updateEndConditions(){
  dict = {
    "indicate1": document.getElementById('indikator-1').value,
    "name1": document.getElementById('exist-label-1').value,
    "indicateA": document.getElementById('indikator-1').value,
    "nameA": document.getElementById('coincide-label-A').value,
    "indicateB": document.getElementById('indikator-1').value,
    "nameB": document.getElementById('coincide-label-B').value,
  }
  $.ajax({
    type: 'POST',
    url: '/updateEndConditions', // Replace with the actual route on your Bottle server
    data: dict, // Pass the formData object directly
    success: function(response) {

    },
    error: function(xhr, status, error) {
      // Handle errors
      console.error('Error:', error);
    }
  });
  // osvezi('pisek-iframe');
}

function downloadFiles() {
  var zip = new JSZip();
  var filePromises = [];

  // Fetch the first file
  filePromises.push(fetch("views/naloga.html")
    .then(response => response.text())
    .then(fileContent => {
      // Add the first file content to the ZIP archive
      zip.file("index.html", fileContent);
    }));

  // Fetch the second file
  filePromises.push(fetch("static/javascript/theTest.js")
    .then(response => response.text())
    .then(fileContent => {
      // Add the second file content to the ZIP archive
      zip.file("task.js", fileContent);
    }));

  Promise.all(filePromises)
    .then(() => {
      // Generate the ZIP file asynchronously
      return zip.generateAsync({ type: "blob" });
    })
    .then(content => {
      // Create a temporary <a> element to trigger the download
      var link = document.createElement('a');
      link.href = URL.createObjectURL(content);
      link.download = "files.zip";
      link.click();

      // Clean up the temporary URL object
      URL.revokeObjectURL(link.href);
    })
    .catch(error => {
      console.error("Error zipping and downloading files:", error);
    });
}

// INFO icon

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})
