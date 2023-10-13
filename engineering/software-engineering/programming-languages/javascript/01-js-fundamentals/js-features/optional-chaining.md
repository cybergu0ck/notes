# Optional Chaining

The code here might look like we are trying to get sam's review if the review is not present we are setting a default value "sam has no review". However we get the error because `myObject.reviews.sam` itself is undefined and hence `myObject.reviews.sam.review` is trying to access review property of undefined.

```js
const myObject = {
  book: "alchemist",
  author: "paulo coelho",
  genre: "fiction",
  reviews: {
    adhiti: {
      rating: 5,
      review: "Paulo Coelho at his best",
    },
    lucy: {
      rating: 4,
      review: "wonderful book",
    },
    jack: {
      rating: 2,
      review: "I read only 2 pages",
    },
  },
};

const samReview = myObject.reviews.sam.review ?? "sam has no review";

console.log(samReview);

//TypeError: Cannot read properties of undefined (reading 'review')
```

<br>

We can avoid the above case by using optional chaining.

```js
const myObject = {
  book: "alchemist",
  author: "paulo coelho",
  genre: "fiction",
  reviews: {
    adhiti: {
      rating: 5,
      review: "Paulo Coelho at his best",
    },
    lucy: {
      rating: 4,
      review: "wonderful book",
    },
    jack: {
      rating: 2,
      review: "I read only 2 pages",
    },
  },
};

const samReview = myObject?.reviews.sam?.review ?? "sam has no review";

console.log(samReview);

//sam has no review
```
