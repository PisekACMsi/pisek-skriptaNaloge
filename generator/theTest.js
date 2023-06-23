function initTask(subTask) {
 subTask.gridInfos = {
     sl: {},
     backgroundColour: "white",
     backgroundTile: "",
     borderColour: "black",
     showLabels: true,
     hasGravity: false,
     maxInstructions: 0,
     ignoreInvalidMoves: [
          false
     ],
     border: 0.02,
     cellSide: [
          60
     ],
     numberOfRobots: 1,
     hideControls: [
          {
               restart: false,
               saveOrLoad: false,
               loadBestAnswer: false,
               speedSlider: false,
               backToFirst: false,
               nextStep: false,
               goToEnd: false
          }
     ],
     zoom: [
          {
               controls: true,
               scale: 1
          }
     ],
     startingExample: [
          {
               blockly: ""
          }
     ],
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