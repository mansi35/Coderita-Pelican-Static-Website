Title: Execution in the Kingdom of Nouns
Date: 2020-12-05 08:30
Modified: 2020-12-05 14:30
Category: Java
Tags: programming
Slug: my-super-post3
Authors: Mansi Sharma
Summary: What's really happening in Javaland?

<div style="text-align:center"><img src="../images/noun.jpg"></div>

In reference to the story given in article <a href="http://steve-yegge.blogspot.com/2006/03/execution-in-kingdom-of-nouns.html">Execution in the Kingdom of Nouns</a>

__1. In context of the article what do the words__

__a. Nouns__

__b. Verbs__

__c. Adjectives__ 

__refer to? Give reasons for your answers and use code examples to support your answer.__

Well, from what I understood, in the blog, the objects are referred to as nouns, the functions as verbs and the attributes are the adjectives.

The main thing, the author wants to convey through his blog is that Java relies very much on objects than anything else. And for sure it gives a well built structure to the program but its maintenance becomes difficult.

In Java, nouns i.e. objects are very important and verbs i.e. functions are given a very low status. Verbs are owned by Nouns. But they're not mere pets; no, Verbs perform all the chores and manual labor in the entire program. They are, in effect, the slaves, or at very least the serfs and indentured servants. And even though all the manual labor is done by them, still they are not allowed to roam freely. A noun must always accompany them. Let’s try to understand it better with the help of an example:

*__Example 1:__*

One day a farmer came to one of the noun and asked him to understand his inventory and told him “Hey Noun, can you design a course of action to find all green apples in my inventory”. Noun replied “Oh Farmer it’s damn easy. I will do it for you, no worries”. The noun writes an extensive procedure and showed it to the Farmer.

    $ Class AppleFilterByColor {
	$    public static List<Apple> filterGreenApples(List<Apple> inventory){
	$	    List<Apple> result = newArrayList<>();
	$	    for(Apple apple: inventory){
	$		    if(“green”.equals(apple.getColor())){
	$			    result.add(apple);
	$		    }
    $        }      
    $        return result;
	$    }
    $ }


Here you can see that apple is a noun (an object) and getColor() is a verb (a function) and the noun always accompanies the verb everywhere. Here result is also a noun, which is the list of all green apples and add() is a verb accompanied by result.

*__Example 2:__*

Farmer got happy and returned to home but, next day he again came to noun and said "Hey Noun, can you design that procedure more flexible so that I can find apples of any color I want. And it would be really cool to differentiate between light apples and heavy apples. Heavy apples have a weight greater than 150 g". Noun replied "Sure!”. He made changes and showed it to the farmer.

    $ Class AppleFilter {
	$    public static List<Apple> filter (List<Apple> inventory, string color, int weight, boolean flag){
    $        List<Apple> result = newArrayList<>();
	$	    for (Apple apple: inventory){
	$		    if ((flag && apple.getColor().equals(color)) || (!flag && apple.getweight() > weight)){
	$			    result.add(apple);
	$		    }
    $        }
    $        return result;
	$    }
    $ }

Now the changes the farmer is asking for again and again i.e. the color and weight of apple, these are the adjectives i.e. the attributes of a particular apple (object).

Now the farmer can use it as follows:

    $ List<Apple> greenApples = filterApple.filter(inventory, “green”, 0, true)
    $ List<Apple> heavyApples = filterApple.filter(inventory, “”, 150, false)

But what we can finally conclude from this is, the noun completely reduced the verbosity of the procedure. The farmer can’t figure out what is this true and false. And if the farmer needs some more adjectives to describe his apples, it would become a really complicated task for the noun.

And to be precise, if the farmer had approached a verb for this task he could have made it a lot simpler by generalizing the attributes.


__2. From the many comments on the article, summarize one comment in favor of the article and one against.__

Favor:

Well it’s easier for everyone if a program is understandable i.e. it is written in such a way that we can understand it without any need for its documentation. For example when visiting a new place it's easier to follow the instruction that directs you how you can go there than finding objects of which state and behavior are unfamiliar to you. Thatswhy, Google maps always tells us the directions and not something like when you see a red letter box do this.
Also taking care of attributes and at the same time maintaining the verbosity of the code is also important and due to this noun oriented thinking of Java it makes it more and more difficult. You just can’t have all the adjectives you want and at the same time keep your program a verbose one.

Against:

Well, Java's constructs enforce better discipline than of C/C++. The modern order requires better stability and security than just speed. And Java surely takes care of that. The structure of a Java code is really a well built one.  This feeling is reinforced when we try to make any changes to the structure; the architectural strength then becomes daunting enough that nobody could bring this structure down. And of course we don’t want our technologies of national importance like missiles or our banking system to fail, just because there was an invalid pointer or memory fault. 
If the programming construct means that I take a bit more effort to express my verbs or the program runs 3 times slower, I'm fine with it than the alternate involving crashing of my nuclear reactors and banks.
Also, being noun oriented is required by OOP, so the real problem here is not Java but the methodologies of OOP, since Java is just following what OOP dictates.

<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
/*
var disqus_config = function () {
this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};
*/
(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');
s.src = 'https://coderita.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
                            
