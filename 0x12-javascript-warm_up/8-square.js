#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
    console.log('Missing size');
} else {
    const sqPrint = Number(process.argv[2]);
    let cnt = 0;
    while (cnt < sqPrint) {
	console.log('X'.repeat(sqPrint));
	cnt++;
    }
}
