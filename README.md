                                                              IITD Buddy

Basic Roadmap of our project is as follows,

- We collected data related to IITD from various resources (, BSP IITD, Quora, Yash Agarwal drives, Har ashish arora drives, BSW fresher resources, IITD main website, Inception Magazine, Reddit)

-We converted the raw data which was mainly in .txt form to small chunks which were then efficiently tagged according to relevance with help of LLM(llama-3.3-70b-versatile) and then stored them as vector points in Qdrant 

 (#Problems faced in this step - #tokens excceded 
  # Solution -   For this we feeded the data by breaking it into some ~ 35 parts ( each part had about 5000 tokens)
 )

-Then on the frontend we made a website using streamlit 

- We wrote a code which was had access to our data points in Qdrant. In that code we took query as input from the user(at the front end). The query after being converted to vector was searched for similarity based on cosine distance using all the vectors in our Qdrant data set.

- The top 20 similar vectors were retrieved as "retrieved_context"

- Then this "retrieved_context" and "query" was given to LLM(llama-3.3-70b-versatile) and the llm was prompted to function as an assistant to a user and give output based on "retrieved_context" and "query" 



-
