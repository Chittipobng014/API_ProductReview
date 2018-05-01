# API_ProductReview

<h2>To Get all review(GET):</h2> <li>https://pacific-peak-27279.herokuapp.com/api/ProductReview/</li>

<h2>To Insert review(POST):</h2> <li>https://pacific-peak-27279.herokuapp.com/api/ProductReview/</li>
* JSON From require {	"productID":[productID],	"rating":[rating],	"comment":[comment], "reviewer": [username]} <br>
* ex. <pre>{
        "productID": 50,
        "rating": 4, 
        "comment": "Hello",
        "reviewer": "Army"
}</pre>
* rating should be 0 to 5
