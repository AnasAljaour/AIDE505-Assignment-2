express = require('express')
bodyParser = require('body-parser')
axios = require('axios')
application = express()
application.use(bodyParser.json())

application.post('/analyze-sentiment', (req, res) =>{
    if(!req.body.text){
        return res.status(400).json({ error: 'Text is required'})
    }
    const text = req.body.text
    axios.post("http://flask-api:5000/predict", { "text" : text})
    .then(response =>{
        if(!response.data.sentiment){
            return res.status(400).send({ error: 'Invalid sentiment response'})
        }
        res.send({ sentiment: response.data.sentiment})
    })
})
application.listen(3000, () =>{
    console.log('Server is running on port 3000')
})
