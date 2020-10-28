# Challenge #12

In this challenge, we are given a bad formatted html code as,

```
<html><body><div class=1>Hello<p>This</p><a href="www.google.com">is a bad formatted<li>code</li></a></div></body></html>
```

And we want to format it to,

```
<html>
 <body>
  <div class="1">
   Hello
   <p>
    This
   </p>
   <a href="www.google.com">
    is a bad formatted
    <li>
     code
    </li>
   </a>
  </div>
 </body>
</html>
```

Write a program named ```formatting.py``` to implement this demand.


To test your result, run:
```
$ source checker.sh
```