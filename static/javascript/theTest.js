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
     maxInstructions: 666,
     includeBlocks: {
          groupByCategory: true,
          generatedBlocks: {
               robot: [
                    "move",
                    "moveSimple"
               ]
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
     backgroundTile: "tiles/trava.png",
     borderColour: "#000000",
     showLabels: false,
     cellSide: 60,
     numberOfRobots: 1,
     itemTypes: {
          sat: {
               num: 4,
               img: [
                    "objects/honeycomb_empty.png",
                    "objects/honeycomb_full.png"
               ],
               zOrder: 2,
               category: [
                    {
                         "sat": true
                    }
               ],
               value: 0,
               nbStates: 8,
               color: [],
               id: 0
          },
          robot0: {
               img: "characters/bee_all_8_sides.png",
               zOrder: 8,
               value: 0,
               nbStates: 9,
               category: {
                    "robot": true
               }
          },
          button_0: {
               img: [
                    "buttons/",
                    "buttons/"
               ],
               num: 5,
               zOrder: 3,
               value: 0,
               id: 0,
               category: {
                    "button": true
               }
          }
     }
};
subTask.data = {
     easy: [
          {
               tiles: [[1, 1, 1, 1, 1, 1, 4], 
 [1, 1, 1, 1, 1, 1, 4], 
 [1, 1, 1, 1, 1, 1, 4]],
               initItems: [
                    {
                         row: 0,
                         col: 6,
                         type: "sat",
                         dir: 0,
                         value: 0
                    },
                    {
                         row: 1,
                         col: 6,
                         type: "sat",
                         dir: 0,
                         value: 0
                    },
                    {
                         row: 2,
                         col: 6,
                         type: "sat",
                         dir: 0,
                         value: 0
                    },
                    {
                         row: 0,
                         col: 0,
                         type: "robot0",
                         dir: 0,
                         value: 0
                    },
                    {
                         row: 0,
                         col: 6,
                         type: "button_0",
                         dir: 0,
                         value: 0
                    },
                    {
                         row: 1,
                         col: 6,
                         type: "button_0",
                         dir: 0,
                         value: 0
                    },
                    {
                         row: 2,
                         col: 6,
                         type: "button_0",
                         dir: 0,
                         value: 0
                    }
               ]
          }
     ]
};
initBlocklySubTask(subTask); 
}