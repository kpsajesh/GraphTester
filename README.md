This project is to create testcases automatically from the requirement document using Gen AI capabilities [such as LLM, LANGRAPH, Human In The Loop (HITL)] and post to Test rail.
Features in detail:
  1. Requirements where testcases to be created are kept in a txt file >  So it is NOT HARDCODED, so can generate testcases for any requirement by paste the requirement in this txt file
    <img width="1097" height="280" alt="image" src="https://github.com/user-attachments/assets/5d2212dd-c04f-49f2-ad8a-018d2e32d687" />

  2. Then the system prompt & user prompt is created
     <img width="1019" height="503" alt="image" src="https://github.com/user-attachments/assets/155176f8-6c27-4163-a0ee-eec35b30ffc9" />

  3. User prompt
    <img width="833" height="504" alt="image" src="https://github.com/user-attachments/assets/e1493b79-5383-4a32-82e8-0d343ff9970d" />

  4. Now the state is defined
    <img width="1327" height="780" alt="image" src="https://github.com/user-attachments/assets/e62067a1-1e29-44cc-83d0-7fff764a083e" />
     
  5. Then the nodes are defined with retry and fallback mechanism
     <img width="1599" height="937" alt="image" src="https://github.com/user-attachments/assets/19b2a013-e1cc-43af-ac69-566e510753db" />

  6. Then the graph is defined with Human In The Loop (HITL)
     <img width="1122" height="854" alt="image" src="https://github.com/user-attachments/assets/88a4d9d3-e6ce-41da-aafb-81e77fe3fa15" />
     
  7.  Building the graph with nodes, edges and conditional edges
    <img width="1109" height="769" alt="image" src="https://github.com/user-attachments/assets/83371a80-3cc1-4d5c-b754-ab5bd5b56b4e" />
     
  8.  Calling the build graph from the main / runner file
     <img width="1365" height="964" alt="image" src="https://github.com/user-attachments/assets/4fbbe9dd-6f79-4701-8fd3-7bbbcb4e0acf" />

  9.  Executing the testcase generator and prompting for the testcase approval or reject
      <img width="1025" height="348" alt="image" src="https://github.com/user-attachments/assets/a27fe440-7556-4e88-b62a-8f88570605ed" />

  10.  Test cases are created as json and csv for verification
      <img width="1329" height="564" alt="image" src="https://github.com/user-attachments/assets/a46cb8fc-f248-4f2a-b33b-70d1dd646032" />
      
  11. So the approver verifies testcases and approves > it creates testcases in Testrails system via API
      <img width="668" height="499" alt="image" src="https://github.com/user-attachments/assets/02040243-4593-43c1-b4d7-648c27f0d273" />
      
  12. Finally the newly created testcases reflects in the demo testcase UI
      <img width="1408" height="968" alt="image" src="https://github.com/user-attachments/assets/5601396b-c6de-470e-b129-242cddfcb31c" />
  
  13. This project also Takes the Testcases > then the issues created on testing are created to the JIRA & SLCK channel via API.
  

  
