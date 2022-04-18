Q1-Extract all karakas and their respective vibhaktis along with sentences from a Hindi treebank.

==============================================================================================

As per my understanding SSF Tree banks having four column seprated by "tab" Namely:
1-Address, 2-Token, 3-Category, 4-Attribute-value pairs
 
4-Attribute-value pairs:
This column contained the the Feature Structure tag <fs> -
<fs> tag having abbreviated attributes or called 'af'.
The field for each attribute is at a fixed position, and a comma is used as a separater.
Thus, in case, no value is given for a particular attribute the field is left blank.
Fixed position of each attribute-
        1-> Root
        2-> Cat
        3-> Gender
        4-> Number
        5-> Person
        6-> Case
        7-> Case Marker/Vibhakti
        8-> Suffix 

Interlinking of nodes:
Nodes might be interlinked with each other through directed edges. Usually, these edges have nothing to do with phrase structure tree, and are concerned with dependency structure, thematic structure, etc. These are specified using the attribute value syntax, how ever, they do not specify a property for a node, rather a relation between two nodes.

```
- So as per question requirment we have to do following task--
    - Extract the 'KARAKAS' from the <fs> tag using keyword "drel", drel represent dependency relation between nodes.
    - Extract 'VIBHAKTI' from the af. In af 'Case Marker/Vibhakti' on 7th postion. 
```

#	Following Assumption I have made:
	######	Output Format:
	```
			#Sentence_ID \t Karak_Name \t Vibhakti \t Vibhakti_Count \t Sentence
			1	k2p	 के	1	हस्तिनापुर जाने के लिए हमने दिल्ली में कश्मीरी गेट बस अड्डे से जाना सुविधाजनक समझा ।
			36, 35, 15, 13, 1	rt	 के लिए	5	श्वेतांबर ट्रस्ट धर्मशाला में ठहरने के लिए 400 कमरे NULL और सुबह के नाश्ते , दोपहर के लंच और रात के भोजन की व्यवस्था होती है ।
			1	k1	 में	1	हस्तिनापुर जाने के लिए हमने दिल्ली में कश्मीरी गेट बस अड्डे से जाना सुविधाजनक समझा ।
			49, 48, 40, 36, 31, 23, 23, 21, 19, 12, 11, 10, 9, 8, 7, 6, 1	k7p	 में	17	तिजारा अतिशय क्षेत्र में चंद्र प्रभु भगवान की सफेद रंग की अत्यंत मनोहारी संगमरमर की मूर्ति स्थापित है ।
			51, 51, 48, 46, 40, 40, 26, 24, 18, 18, 18, 11, 10, 10, 6, 1	nmod		16	बताते हैं कि तिजारा क्षेत्र के एक मशहूर वैद्य बिहारी लाल की पत्‍नी सरस्वती देवी ने तीन दिन का उपवास रखा था ।
			4, 3, 2, 1	k5	 से	4	दिल्ली से हस्तिनापुर की दूरी तकरीबन 105 किलोमीटर है ।
			51, 51, 47, 44, 32, 31, 30, 29, 28, 27, 24, 15, 15, 14, 6, 1	k2		16	बताते हैं कि तिजारा क्षेत्र के एक मशहूर वैद्य बिहारी लाल की पत्‍नी सरस्वती देवी ने तीन दिन का उपवास रखा था ।
	```
				
######	Follow the following steps to execute the programs:
		Extaract the Directory with name 'NLP-Internship-V0.2'
		$ cd NLP-Internship-V0.2
		$ python3 karak_vibhakti_extractor-v2.py ssf_file_name

## For example
		$ cd NLP-Internship-V0.2
		$ python3 karak_vibhakti_extractor-v2.py Data/mor-1-50-posn-name.txt > output.csv

Version-0.2
Auther- Vilal Ali

Thanks for using program, Enjoy!
