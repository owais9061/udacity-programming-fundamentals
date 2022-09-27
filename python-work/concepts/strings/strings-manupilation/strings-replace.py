# Let's go over another string method: string.replace. Use this method
# to replace the instance of NOUN with "duck" and VERB with "waddle" in the string
# sentence. 
# single identity (ID)
# class identity 

sentence = "A NOUN went on a walk. They can VERB really well.";
sentence = sentence.replace("NOUN", "Owais");
sentence= sentence + sentence.replace("VERB","RUN")
print(sentence);