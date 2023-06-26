function initTask(subTask) {
 subTask.gridInfos = {
     languageStrings: {
          sl: {
               options: {
                    tools: {
                         bool: {
                              robot: "Pastirček"
                         }
                    }
               },
               label: {
                    transport: "%1 Pastirčka"
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
     maxInstructions: 30,
     ignoreInvalidMoves: false,
     border: 0.02,
     backgroundColour: "#000000",
     backgroundTile: "tiles/trava.png",
     borderColour: "#000000",
     showLabels: false,
     cellSide: 60,
     numberOfRobots: 1,
     startingExample: {
          blockly: ""
     },
     checkEndEveryTurn: false,
     includeBlocks: {
          groupByCategory: true,
          generatedBlocks: {
               robot: [
                    "move",
                    "moveSimple",
                    "forwardSimple",
                    "turn",
                    "transport",
                    "sensorBool"
               ]
          },
          standardBlocks: {
               includeAll: false,
               wholeCategories: [
                    "logic",
                    "loops",
                    "variables"
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
          obstacle_1: {
               num: 2,
               category: [
                    {
                         'obstacle': true
                    }
               ],
               img: [
                    "objects/drevo.png"
               ],
               zOrder: 5,
               id: 0
          },
          obstacle_2: {
               num: 3,
               category: [
                    {
                         'obstacle': true
                    }
               ],
               img: [
                    "objectsUser/obstacleUser.png"
               ],
               zOrder: 5,
               id: 0
          },
          image_1: {
               num: 4,
               category: [
                    {
                         'image': true
                    }
               ],
               img: [
                    "objects/cesta_navzgor.png"
               ],
               zOrder: 2,
               id: 0
          },
          image_2: {
               num: 5,
               category: [
                    {
                         'image': true
                    }
               ],
               img: [
                    "objects/cesta_ovinek1.png"
               ],
               zOrder: 2,
               id: 0
          },
          image_3: {
               num: 6,
               category: [
                    {
                         'image': true
                    }
               ],
               img: [
                    "objects/cesta_ovinek2.png"
               ],
               zOrder: 2,
               id: 0
          },
          image_4: {
               num: 7,
               category: [
                    {
                         'image': true
                    }
               ],
               img: [
                    "objects/cesta_ovinek3.png"
               ],
               zOrder: 2,
               id: 0
          },
          image_5: {
               num: 8,
               category: [
                    {
                         'image': true
                    }
               ],
               img: [
                    "objects/cesta_ovinek4.png"
               ],
               zOrder: 2,
               id: 0
          },
          image_6: {
               num: 9,
               category: [
                    {
                         'image': true
                    }
               ],
               img: [
                    "objects/cesta_vodoravna.png"
               ],
               zOrder: 2,
               id: 0
          },
          robot_1: {
               category: [
                    {
                         'robot': true
                    }
               ],
               img: [
                    "characters/avto.png"
               ],
               zOrder: 10,
               nbStates: 8,
               id: 0
          },
          robot_2: {
               category: [
                    {
                         'robot': true
                    }
               ],
               img: [
                    "characters/bee_all_8_sides.png"
               ],
               zOrder: 10,
               nbStates: 8,
               id: 0
          }
     }
};
subTask.data = {
     easy: [
          {
               tiles: [[1, 2, 2, 2, 2, 2, 2, 2], 
 [3, 2, 2, 2, 2, 2, 9, 6], 
 [5, 9, 9, 9, 6, 1, 2, 4], 
 [4, 1, 1, 1, 4, 1, 2, 4], 
 [4, 1, 1, 1, 8, 9, 9, 7], 
 [4, 1, 1, 2, 2, 2, 2, 1], 
 [4, 1, 1, 1, 2, 2, 2, 1]],
               initItems: [
                    {
                         type: "obstacle_1",
                         row: 1,
                         col: 0,
                         dir: 0
                    },
                    {
                         type: "robot_1",
                         row: 6,
                         col: 0,
                         dir: 0
                    },
                    {
                         type: "robot_2",
                         row: 2,
                         col: 3,
                         dir: 0
                    }
               ]
          }
     ]
};
initBlocklySubTask(subTask); 
}