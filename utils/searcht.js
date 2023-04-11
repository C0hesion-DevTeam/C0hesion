function levenshteinDistance(a, b) {
    const matrix = [];

    for (let i = 0; i <= b.length; i++) {
        matrix[i] = [i];
    }

    for (let i = 0; i <= a.length; i++) {
        matrix[0][i] = i;
    }

    for (let i = 1; i <= b.length; i++) {
        for (let j = 1; j <= a.length; j++) {
            if (b.charAt(i - 1) === a.charAt(j - 1)) {
                matrix[i][j] = matrix[i - 1][j - 1];
            } else {
                matrix[i][j] = Math.min(matrix[i - 1][j - 1] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j] + 1);
            }
        }
    }

    return matrix[b.length][a.length];
}

function sortDictionaryByTeamtypeSimilarity(inputString, inputDict) {
    const dictEntries = Object.entries(inputDict);

    dictEntries.sort((a, b) => {
        const aDistance = levenshteinDistance(inputString, a[1].teamtype);
        const bDistance = levenshteinDistance(inputString, b[1].teamtype);

        return aDistance - bDistance;
    });

    const sortedDict = Object.fromEntries(dictEntries);
    return sortedDict;
}


function formatInputObject(arr) {
    const formattedObj = {};

    for (let i = 0; i < arr.length; i++) {
        const key = `item${i}`;
        formattedObj[key] = arr[i];
    }

    return formattedObj;
}

function searchTeach(searchtext){
    var curd
    fetch('http://127.0.0.1/teamtable')//url 到时候改一下，调试的时候就用回网号吧
        .then(response => response.text())
        .then(csv => {
            const rows = csv.trim().split('\n');
            const headers = rows[0].split(',');
            const data = rows.slice(1).map(row => {
                const values = row.split(',');
                return headers.reduce((obj, header, i) => {
                    obj[header] = values[i];
                    return obj;
                }, {});
            });
            //console.log(data);
            curd=data
            const sortedEntries = Object.entries(sortDictionaryByTeamtypeSimilarity(searchtext,formatInputObject(curd)));
            //console.log(sortedEntries)
            return sortedEntries
        })
        .catch(error => console.error(error));





}
var searchResults
searchTeach(searchtext)
    .then(sortedEntries => {
        searchResults=sortedEntries;//这个是个列表，可以直接从【0】，【1】，【2】     开始访问

        //enter further code here








    })
    .catch(error => {
        console.error(error);
    });


