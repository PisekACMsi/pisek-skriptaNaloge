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
     maxInstructions: 0,
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
               robot: []
          },
          standardBlocks: {
               includeAll: false,
               wholeCategories: [],
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
               category: [
                    {
                         'robot': true
                    }
               ],
               img: [
                    "characters/marta_in piki.png"
               ],
               zOrder: 10,
               nbStates: 8
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