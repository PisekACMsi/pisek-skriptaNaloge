function initTask(subTask) {
 subTask.gridInfos = {
     languageStrings: {
          sl: {}
     },
     hideControls: {
          restart: false,
          saveOrLoad: false,
          loadBestAnswer: false,
          speedSlider: false,
          backToFirst: false,
          nextStep: false,
          goToEnd: false
     },
     hasGravity: false,
     introMaxHeight: "33%",
     maxListSize: 100,
     scrollbars: true,
     zoom: {
          controls: true,
          scale: 1
     },
     actionDelay: 400,
     blocklyColourTheme: "bwinf",
     maxInstructions: 0,
     includeBlocks: {
          groupByCategory: true,
          generatedBlocks: {
               robot: []
          },
          standardBlocks: {
               includeAll: false,
               wholeCategories: [],
               singleBlocks: [],
               excludedBlocks: []
          }
     },
     startingExample: {
          blockly: ""
     },
     checkEndEveryTurn: false,
     checkEndCondition: (context, lastTurn) => { 
	robotEndConditions.checkCombiner(context, lastTurn, [
		//,
		//
	])
},
     ignoreInvalidMoves: false,
     border: 0.02,
     backgroundColour: "#000000",
     backgroundTile: "tilesUser/image_image.png",
     borderColour: "#000000",
     showLabels: false,
     cellSide: 60,
     numberOfRobots: 1,
     itemTypes: {
          robot0: {
<<<<<<< HEAD
               img: "characters/avto.png",
=======
               img: "charactersUser/image_image.png",
>>>>>>> b46826f0fcf71ae12988ab7b6fe351804e5b3957
               zOrder: 20,
               value: 0,
               nbStates: 9,
               category: {
                    "robot": true
               }
          },
          obstacle0: {
               num: 4,
<<<<<<< HEAD
               img: "objects/banana.png",
               zOrder: 2,
=======
               img: "objectsUser/image_imageUser.png",
               zOrder: 2,
               category: {
                    "obstacle": true
               },
               value: 0
          },
          obstacle1: {
               num: 5,
               img: "objectsUser/image_image.png",
               zOrder: 3,
>>>>>>> b46826f0fcf71ae12988ab7b6fe351804e5b3957
               category: {
                    "obstacle": true
               },
               value: 0
          },
          Ime: {
               num: 6,
               img: [
                    "objectsUser/image_image.png"
               ],
               zOrder: 2,
               category: [],
               value: 0,
               color: [],
               id: 1
          }
     }
};
subTask.data = {
     easy: [
          {
<<<<<<< HEAD
               tiles: [[1, 1, 1, 1, 1], 
=======
               tiles: [[4, 1, 1, 1, 1], 
>>>>>>> b46826f0fcf71ae12988ab7b6fe351804e5b3957
 [1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1]],
               initItems: [
                    {
                         row: 0,
<<<<<<< HEAD
                         col: 0,
=======
                         col: 1,
>>>>>>> b46826f0fcf71ae12988ab7b6fe351804e5b3957
                         type: "robot0",
                         dir: 0,
                         value: 0
                    }
               ]
          }
     ]
};
initBlocklySubTask(subTask); 
}