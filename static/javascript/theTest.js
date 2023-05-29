function initTask(subTask) {
 subTask.gridInfos = {
     languageStrings: {
          sl: {
               categories: {
                    actions: "Gibanje"
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
     introMaxHeight: "33%",
     maxListSize: 100,
     scrollbars: true,
     zoom: {
          controls: true,
          scale: 1
     },
     actionDelay: 400,
     blocklyColourTheme: "bwinf",
     maxInstructions: 2,
     includeBlocks: {
          groupByCategory: false,
          generatedBlocks: {
               robot: [
                    "ForwardSimple"
               ]
          },
          standardBlocks: {
               includeAll: false,
               wholeCategories: [
                    "Lists",
                    "Loops"
               ],
               singleBlocks: [],
               excludedBlocks: []
          }
     },
     startingExample: {
          blockly: ""
     },
     checkEndEveryTurn: true,
     checkEndCondition: (context, lastTurn) => { 
	robotEndConditions.checkCombiner(context, lastTurn, [
		(context, lastTurn) => { robotEndConditions.checkItemExistence(context, lastTurn, {category: "coin"}, {}, exist=false) },
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
     numberOfRobots: 1,
     itemTypes: {
          objekt_0: {
               num: 2,
               img: "",
               zOrder: 2,
               category: [],
               value: 0
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
                         type: "objekt_0",
                         dir: 0,
                         value: 0
                    }
               ]
          },
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