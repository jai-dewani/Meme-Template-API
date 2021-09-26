# Meme Template API

This is a API created for my [memeify](https://github.com/jai-dewani/memeify) project which needs an API t get a list of images that are meme template with meta data about the meme. Feel free to use it for your personal projects, I would love to see what all different ideas people can come up with this projects! 

> It is currently in development phase, not hosted anywhere. Will update this when this changes 🤞

## Contribute 

Feel free to add your contribution. You can contribute in the following ways, like 

- Looking at Issues, and helping me impliment features and solve bugs 
- Have an idea for a cool feature, feel free to open a issue
- Help me increase my meme template list.  
Just add a new entry in the `meme.json` file. Just make sure it has all these parameters
```json 
"id": //Last Meme template entry's ID + 1,
"name": //Common name by which the meme is referred to (if more than one, seprate them using comma),
"url": // Link to the image
"width": // Widht of the image 
"height": // Height of the image,
"box_count": //the standard number of boxes the meme should have for dialogues
```

