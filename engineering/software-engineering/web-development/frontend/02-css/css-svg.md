# SVG

- “SVG” stands for “Scalable Vector Graphics”.
  - Vector graphics are simply images defined by math, as opposed to traditional “raster graphics”, where your image is defined by a grid of pixels.
  - With raster graphics, the detail is limited to the size of that pixel grid. If you want to increase the size of the image (scale it), you have to increase the size of that grid. How do you decide what all those new pixels should look like? There’s no simple solution. Additionally, the larger the grid, the bigger your filesize grows.
- SVGs are defined using XML.
  - XML format is human readable.
  - XML is designed to be interoperable with HTML, which means you can put the above code directly in an HTML file.
- SVGs are great for relatively simple images, but because every single detail of the image needs to be written out as XML, they are extremely inefficient at storing complex images. If your image is supposed to be photo-realistic, or it has fine detail or texture (“grunge textures” are a great example), then SVGs are the wrong tool for the job.

<br>

## Anatomy of SVG

```html
<div class="container">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
    <rect x="0" y="0" width="100" height="100" fill="burlywood" />
    <path
      d="M 10 10 H 90 V 90 L 10 60"
      fill="transparent"
      stroke="black"
      stroke-width="3"
    />
    <circle cx="50" cy="50" r="20" class="svg-circle" />
    <g class="svg-text-group">
      <text x="20" y="25" rotate="10" id="hello-text">Hello!</text>
      <use href="#hello-text" x="-10" y="65" fill="white" />
    </g>
  </svg>
</div>
```

- `xmlns` : stands for “XML NameSpace”. This specifies what dialect of XML you’re using.
- `viewBox` - defines the bounds of your SVG, It also defines the aspect ratio and the origin of your SVG.
- `class`, `id` - these attributes function just like they do in HTML. Using these in SVGs allows you to easily target an element via CSS or JavaScript, or to reuse an element via the use element.
- Elements such as `<circle>`,` <rect>`, `<path>`, and `<text>` are defined by the SVG namespace. These are our basic building-blocks.

<br>

## Embedding SVG

- There are two main approaches when deciding how to actually place the SVG in your document: _linked_, and _inline_.

1. Linking SVGs works basically the same way as linking any other image.
   - We can use an HTML image element such as `<img>`, or link it in your CSS using `background-image: url(./my-image.svg)`.
   - They will still scale properly, but the contents of the SVG will not be accessible from the webpage.
2. inline SVGs works by pasting their contents directly into your webpage’s code.
   - The SVG’s properties will be visible to your code, which will allow you to alter the image dynamically via CSS or JavaScript.
   - However, It makes the code harder to read, makes the page less cacheable, and if it’s a large SVG it might delay the rest of your HTML from loading.
   - Some of the drawbacks of inlining SVG code can be avoided once you’ve learned a front-end JavaScript library like React, or a build-tool like webpack.

<br>

## SVG Libraries

- https://fonts.google.com/icons
- https://feathericons.com/
- https://thenounproject.com/browse/icons/term/free/
- https://ionic.io/ionicons

<br>
<br>
