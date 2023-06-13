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
                    "sensorBool",
                    "sensorValue"
               ]
          },
          standardBlocks: {
               includeAll: false,
               wholeCategories: [
                    "tools",
                    "logic",
                    "loops",
                    "math",
                    "texts",
                    "lists",
                    "colour",
                    "variables",
                    "functions"
               ],
               singleBlocks: [
                    "math_arithmetic"
               ],
               excludedBlocks: []
          }
     },
     startingExample: {
          blockly: ""
     },
     checkEndEveryTurn: false,
     checkEndCondition: (context, lastTurn) => { 
	robotEndConditions.checkCombiner(context, lastTurn, [
		(context, lastTurn) => { robotEndConditions.checkItemExistence(context, lastTurn, {category: "coin"}, {}, exist=false) },
		//
	])
},
     ignoreInvalidMoves: false,
     border: 0.02,
     backgroundColour: "#000000",
     backgroundTile: "asfalt.png",
     borderColour: "#000000",
     showLabels: false,
     cellSide: 60,
     numberOfRobots: 1,
     itemTypes: {}
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