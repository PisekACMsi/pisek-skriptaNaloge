function initTask(subTask) {
 subTask.gridInfos = {
     languageStrings: {
          sl: {
               label: {
                    alterValue1D: "bla",
                    sensorValue: "bla"
               },
               options: {
                    tools: {
                         bool: {
                              colour: "bla"
                         }
                    }
               }
          }
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
     zoom: {
          controls: true,
          scale: 1
     },
     hasGravity: false,
     introMaxHeight: "33%",
     maxListSize: 100,
     scrollbars: true,
     actionDelay: 400,
     blocklyColourTheme: "bwinf",
     maxInstructions: 10,
     ignoreInvalidMoves: false,
     border: 0.02,
     backgroundColour: "white",
     backgroundTile: "",
     borderColour: "black",
     showLabels: true,
     cellSide: 60,
     numberOfRobots: 1,
     startingExample: {
          blockly: ""
     },
     includeBlocks: {
          groupByCategory: true,
          generatedBlocks: {
               robot: [
                    "moveSimple",
                    "forward",
                    "forwardSimple"
               ]
          },
          standardBlocks: {
               includeAll: false,
               wholeCategories: [
                    "logic",
                    "loops",
                    "math"
               ],
               singleBlocks: [],
               excludedBlocks: []
          }
     },
     checkEndCondition: (context, lastTurn) => { 
	robotEndConditions.checkCombiner(context, lastTurn, [
		//,
		//
	])
},
     itemTypes: {
          obstacle0: {
               num: 3,
<<<<<<< HEAD
=======
               category: [
                    {
                         'obstacle': true
                    }
               ],
               img: [
                    "objects/blok3.png"
               ],
               zOrder: 5
          },
          obstacle1: {
               num: 4,
>>>>>>> 3e58c0e99b5ce7a035a14c798da56069c60e64c7
               category: [
                    {
                         'obstacle': true
                    }
               ],
               img: [
                    "objects/blok3.png"
               ],
               zOrder: 5
          },
          obstacle2: {
               num: 5,
               category: [
                    {
                         'obstacle': true
                    }
               ],
               img: [
                    "objects/blok3.png"
               ],
               zOrder: 5
          },
<<<<<<< HEAD
          number0: {
               num: 4,
=======
          obstacle3: {
               num: 6,
               category: [
                    {
                         'obstacle': true
                    }
               ],
               img: [
                    "objects/blok3.png"
               ],
               zOrder: 5
          },
          obstacle4: {
               num: 7,
               category: [
                    {
                         'obstacle': true
                    }
               ],
               img: [
                    "objects/blok3.png"
               ],
               zOrder: 5
          },
          number0: {
               num: 8,
               category: [
                    {
                         'number': true
                    }
               ],
               zOrder: 4,
               value: "0"
          },
          robot0: {
>>>>>>> 3e58c0e99b5ce7a035a14c798da56069c60e64c7
               category: [
                    {
                         'number': true
                    }
               ],
<<<<<<< HEAD
               zOrder: 4,
               value: "0"
=======
               img: [
                    "characters/marta_in piki.png"
               ],
               zOrder: 10,
               nbStates: 8
>>>>>>> 3e58c0e99b5ce7a035a14c798da56069c60e64c7
          }
     }
};
subTask.data = {
     easy: [
          {
               tiles: [[1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1]],
               initItems: []
          }
     ]
};
initBlocklySubTask(subTask); 
}