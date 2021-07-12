var counts = {}
var keys = [];
function wordCounter(str)
{
    var lowerWords = str.toLowerCase();
    var words_split = lowerWords.split(/\W+/);
    console.log(words_split);

    for(var i = 0; i < words_split.length; i++)
    {
        var word = words_split[i].toLowerCase();
        console.log(word);
        if (!/\d+/.test(word))
        {
            if(counts[word] === undefined)
            {
                counts[word] = 1;
                keys.push(word);
            }
            else
            {
                counts[word] = counts[word] + 1;
            }
        }
        
        console.log(counts)
    }  
    
}
keys.sort()

for(var i=0; i < keys.length; i++)
{
    var keys = keys[i];
    createDiv(key + " " + counts[key]);
}



wordCounter("Chaitanya Mohite Mohite Chaitanya Praksah Mohite Mohite");


