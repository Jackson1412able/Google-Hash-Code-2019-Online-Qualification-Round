# hashcode-2019
<p>
<img src="https://user-images.githubusercontent.com/46261099/53238758-20ef5300-36d5-11e9-9f02-42b987d23c65.jpg" width="380" height="140" />
</p>
Our Solution for Google Hash Code 2019 Qualification Round.

## Score
Total score: 1,025,552 submission points:

A:  2       points  
B:  186,633 points  
C:  1,403   points  
D:  439,166 points  
E:  398,348 points  

## Approach
This solution implements Greedy Algorithm to tackle the problem. Here are the steps for our approach:
- Parse input, return list of photos
- Sort list of photos according to number of tags in a descending manner
- Group photos into slides, for horizontal photos, 1 photo per slide, for vertical photos, search for photo that has most number of unsimilar tags, combine it in one slide
- Sort list of slides according to number of tags in a descending manner
- Assign first slide to slideshow
- Look for slide that has the most score according to the scoring scheme and append the slide into slideshow, repeat until no slides left in the list of slides

## Usage
Example:
```
python ghc_new.py d_pet_pictures.txt d_pet_pictures.out
```
