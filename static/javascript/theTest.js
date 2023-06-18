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
     backgroundColour: "white",
     backgroundTile: "",
     borderColour: "black",
     showLabels: true,
     cellSide: 60,
     numberOfRobots: 4,
     itemTypes: {
          robot0: {
               img: "characters/avto.png",
               zOrder: 8,
               value: 0,
               nbStates: 9,
               category: {
                    "robot": true
               }
          },
          robot1: {
               img: "characters/cebela.png",
               zOrder: 8,
               value: 0,
               nbStates: 9,
               category: {
                    "robot": true
               }
          },
          robot2: {
               img: "characters/avto.png",
               zOrder: 8,
               value: 0,
               nbStates: 9,
               category: {
                    "robot": true
               }
          },
          robot3: {
               img: "characters/rdec_robot.png",
               zOrder: 8,
               value: 0,
               nbStates: 9,
               category: {
                    "robot": true
               }
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
               initItems: [
                    {
                         row: 0,
                         col: 0,
                         type: "robot0",
                         dir: 0,
                         value: 0
                    },
                    {
                         row: 0,
                         col: 0,
                         type: "robot1",
                         dir: 0,
                         value: 0
                    },
                    {
                         row: 0,
                         col: 0,
                         type: "robot2",
                         dir: 0,
                         value: 0
                    },
                    {
                         row: 0,
                         col: 0,
                         type: "robot3",
                         dir: 0,
                         value: 0
                    }
               ]
          }
     ]
};
initBlocklySubTask(subTask); 
}