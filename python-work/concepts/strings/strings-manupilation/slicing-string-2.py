# Use string slicing to store everything before "Programmer" in substring1,
# everything after "Programmer" and before "run" in substring2, and everything after "Run" 
# in substring3.

sentence = "A Programmer went on a walk. He can Run really fast. Another Run"

#print(sentence.find('Samrah'));
#print(sentence.find('Another'));

substring1 = sentence[0:2]; # A
substring2 = sentence[2:13] #programmer
substring3 = sentence[13:35]; #programmer se lekr Run
substring4 = sentence[35:]; # Run se lekr agay tk

print(substring1, substring2, substring3, substring4);

member="I am a very volunteered member of the organization"
print(member.replace("volunteered", "Owais"));
