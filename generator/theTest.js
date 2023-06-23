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
               includeAll: false
          },
          wholeCategories: [],
          singleBlocks: [],
          excludedBlocks: []
     },
     checkEndCondition: (context, lastTurn) => { 
	robotEndConditions.checkCombiner(context, lastTurn, [
		//,
		//
	])
},
     itemTypes: {
          robot0: {
               num: 0,
               category: [
                    {
                         'robot': true
                    }
               ],
               img: [
                    "characters/avto.png"
               ],
               zOrder: 10,
               nbStates: 8
          },
          obstacle0: {
               num: 1,
               category: [
                    {
                         'obstacle': true
                    }
               ],
               img: [
                    "objects/banana.png"
               ],
               zOrder: 3
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