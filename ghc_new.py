import sys
import math

class Photo():
    def __init__(self,id,orientation,tag):
        self.id=id
        self.orientation=orientation
        self.number_of_tag=int(tag)
        self.tags = []
        self.unsimilarity_count = 0
		
class Slide():
    def __init__(self,id):
        self.id=id
        self.photo_id=[]
        self.tags = []
   
def parse_input(file):
    photo_list=[]
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            if i==0: n_photo=line.split(' ')[0]
            else:
                line = line.strip('\n')
                photo_list.append(Photo(i-1,line.split(' ')[0],int(line.split(' ')[1])))
                counter = 2
                while counter < int(line.split(' ')[1]) + 2:
                    photo_list[i-1].tags.append(line.split(' ')[counter])
                    counter += 1

    return n_photo,photo_list
	
def sort_photo_list(photo_list):
	photo_list.sort(key = lambda x: len(x.tags), reverse = True)

def group_photos_into_slides(photo_list):
	slides = []
	slide_counter = 0
	dummy_counter1 = 0
	
	while len(photo_list) > 0:
		dummy_counter1, slide_counter = loop1(dummy_counter1, photo_list, slides, slide_counter)
	return slides
	
def loop1(dummy_counter1, photo_list, slides, slide_counter):
	print(dummy_counter1)
	dummy_counter1 += 1
	x = photo_list[0]
	photo_list.remove(x)
	if x.orientation == 'V':
		matched_photo = find_photo_with_most_unsimilar_tags(x, photo_list)
		slides.append(Slide(slide_counter))
		slides[slide_counter].photo_id.append(x.id)
		slides[slide_counter].tags.extend(x.tags)
		slides[slide_counter].photo_id.append(matched_photo.id)
		slides[slide_counter].tags.extend(matched_photo.tags)
		slides[slide_counter].tags = list( dict.fromkeys(slides[slide_counter].tags) )
		slide_counter += 1
	elif x.orientation == 'H':
		slides.append(Slide(slide_counter))
		slides[slide_counter].photo_id.append(x.id)
		slides[slide_counter].tags.extend(x.tags)
		slide_counter += 1
	return dummy_counter1, slide_counter
			
def find_photo_with_most_unsimilar_tags(photo, photo_list):
	for y in photo_list:
		loop2(y, photo)
					
	photo_list_ref_sorted = sorted(photo_list, key = lambda j: j.unsimilarity_count, reverse = True)
	photo_list.remove(photo_list_ref_sorted[0])
	return photo_list_ref_sorted[0]
	
def loop2(y, photo):
	y.unsimilarity_count = 0
	if y.id == photo.id:
		return
	elif y.orientation == 'V':
		for g in y.tags:
			if not g in photo.tags:
				y.unsimilarity_count += 1
		for g in photo.tags:
			if not g in y.tags:
				y.unsimilarity_count += 1
	
def sort_slide_list(slides):
	slides.sort(key = lambda d: len(d.tags), reverse = True)
	
def assign_slide_to_slideshow(slides):
	slideshow = []
	dummy_counter = 0
	slideshow.append(slides[0])
	slides.pop(0)
	s1 = slideshow[0]
	
	while len(slides) > 0:
		dummy_counter, s1 = loop3(dummy_counter, slides, s1, slideshow)	
	return slideshow

def loop3(dummy_counter, slides, s1, slideshow):
	print(dummy_counter)
	dummy_counter += 1
	largest_score_slide_id = 0
	largest_score_slide_id_index = 0
	
	for i, s2 in enumerate(slides):
		largest_score_slide_id, largest_score_slide_id_index = loop4(s1, s2, largest_score_slide_id, largest_score_slide_id_index, i)
				
	slideshow.append(slides[largest_score_slide_id_index])
	s1 = slides[largest_score_slide_id_index]
	slides.pop(largest_score_slide_id_index)
	return dummy_counter, s1
	
def loop4(s1, s2, largest_score_slide_id, largest_score_slide_id_index, i):
	score = evaluate_min(s1, s2)
	if score > largest_score_slide_id:
		largest_score_slide_id = score
		largest_score_slide_id_index = i
	return largest_score_slide_id, largest_score_slide_id_index
	
def evaluate_min(s1, s2):
	unique_s1_counter = 0
	intersect_counter = 0
	unique_s2_counter = 0
	for t in s1.tags:
		if not t in s2.tags:
			unique_s1_counter += 1
	for t in s1.tags:
		if t in s2.tags:
			intersect_counter += 1
	for t in s2.tags:
		if not t in s1.tags:
			unique_s2_counter += 1
			
	return min(unique_s1_counter, intersect_counter, unique_s2_counter)

if __name__ == "__main__":
	n_photo, photo_list = parse_input(sys.argv[1]) #photo_list = list of photo classes
	sort_photo_list(photo_list)
	slides = group_photos_into_slides(photo_list)
	sort_slide_list(slides)
	slideshow = assign_slide_to_slideshow(slides)

	with open(sys.argv[2], 'w') as f:
		f.write('{}\n'.format(len(slideshow)))
		for s in slideshow:
			for e in s.photo_id:
				f.write('{} '.format(e))
			f.write('\n')
    
