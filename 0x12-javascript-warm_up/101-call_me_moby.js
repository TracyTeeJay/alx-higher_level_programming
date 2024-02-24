#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
    for (let cnt = 0; cnt < x; cnt++) {
	theFunction();
    }
};
