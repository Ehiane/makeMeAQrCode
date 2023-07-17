def matchingStrings(strings, queries):
    # Write your code here
    #Description of my idea:
    #Since we are to use the input vector to determine how many instances of 
    #each string exists in the query vector. My best advice would be to use an 
    #unordered map(c++) / dictionary (pyhton)
    #use a for loop to initialize all the key's in the dictionary, without duplicates.
    
    #-------------------------------------------------------------------------------
    tally = {}; # initializing the dictionary
    occurences = []; #initializing the list/array
    
    # setting all the values of the keys to zero
    for mKey in range(len(queries)):
        tally[queries[mKey]] = 0; 
    
    #populate the dictionary with the number of its occurences:
    for i in range(len(queries)):
        currentKey = queries[i];

       #loop through the strings array and compare each query element 
       # with all the strings elements

        for j in range(len(strings)): 
            currentString = strings[j];
     
            #compare the currentKey with the Current string;
            if currentKey == currentString: #if they match 
                tally[currentKey] += 1; #increment the tally value
            else: 
                pass;  # move on
    
    #at this point, the tally's of all strings should be updated
    #Assuming the queries elements dont change position, copy the values of the tally keys into occurences.
 
    for key in tally:
        occurences.append(tally[key]);
    return occurences;


def main():
    m_Strings =  ["ab","ab","abc"];
    m_queries = ["ab","abc","bc"];
    return_Tallys = [];
    return_Tallys = matchingStrings(m_Strings,m_queries);
    print(return_Tallys);


main()