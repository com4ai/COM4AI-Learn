# How to Build RAG

RAG stands for **Retrieval-Augmented Generation**. It is a way to help an LLM answer questions using information from your own documents.

For example, a general-purpose LLM may not know your company policy, private notes, or the latest version of a product manual. With RAG, the application finds the most relevant parts of those documents and gives them to the LLM before it answers.

```text
Question: "What is the refund policy?"
                 │
                 ▼
       Find relevant document sections
                 │
                 ▼
       Give the sections to the LLM
                 │
                 ▼
Answer based on the supplied information
```

## Why Use RAG?

An LLM has knowledge from its training, but that knowledge can be incomplete, old, or unrelated to your private data. RAG connects the model to information that you control.

RAG is useful when you need answers based on:

- Company documentation
- Product manuals
- Policies and procedures
- Research papers
- Support articles
- Personal notes
- Frequently changing information

It can also show the source documents used for an answer, which makes the result easier to check.

## RAG vs. Fine-Tuning

RAG and fine-tuning solve different problems.

| | RAG | Fine-tuning |
|---|---|---|
| Main purpose | Give the model access to external knowledge. | Change the model's behavior, style, or task performance. |
| Knowledge updates | Add, edit, or remove documents from the index. | Train the model again. |
| Best for | Current, private, or source-backed information. | Consistent formatting, classification, or a specialized behavior. |
| Source citations | Natural to provide. | Not built in. |
| Cost and speed to update | Usually lower and faster. | Usually higher and slower. |

For a policy document that changes next week, use RAG. For a model that must always produce a specific JSON format, fine-tuning may be useful. A production system can use both.

## How RAG Works

A basic RAG application has two phases: **indexing** and **question answering**.

### 1. Indexing Documents

Before a user asks a question, the application prepares the documents for search.

```text
Documents
   │
   ▼
Extract text
   │
   ▼
Split text into smaller chunks
   │
   ▼
Create an embedding for each chunk
   │
   ▼
Store embeddings, text, and metadata in an index
```

### 2. Answering a Question

When a user asks a question, the application retrieves useful chunks and supplies them as context to the LLM.

```text
User question
   │
   ▼
Create an embedding for the question
   │
   ▼
Search for the most similar document chunks
   │
   ▼
Build a prompt with the retrieved context
   │
   ▼
LLM generates an answer and source references
```

## Core Components

| Component | Purpose |
|---|---|
| **Documents** | The knowledge you want the chatbot to use, such as text files, PDFs, web pages, or database records. |
| **Document loader** | Reads each source and extracts usable text. |
| **Chunks** | Small sections of a document. Searching small sections is more precise than searching an entire book or manual. |
| **Embeddings** | Lists of numbers that represent the meaning of text. Similar meanings are placed close together in embedding space. |
| **Vector store** | Stores chunk embeddings and performs similarity search. It can be a local library, a database, or a managed service. |
| **Retriever** | Finds the chunks most relevant to a question. |
| **Prompt** | Instructions and retrieved context sent to the LLM. |
| **LLM** | Produces a natural-language answer using the retrieved context. |
| **Metadata** | Extra information such as file name, page number, title, URL, or chunk number. It is essential for citations. |

## What Are Embeddings?

An embedding converts text into numbers that capture some of its meaning. The following sentences use different words but have a similar meaning:

```text
"How do I return an item?"
"What is the process for getting a refund?"
```

Their embeddings are likely to be close together. That lets a RAG application find relevant content even when the user's wording does not exactly match the document.

The embedding model searches for relevant content; it does **not** write the final answer. The LLM writes the answer after retrieval.

## Chunking Documents

Chunks are the pieces of text stored and retrieved by the RAG system. A chunk should contain enough context to be meaningful, but not so much unrelated text that it confuses search or wastes the LLM's context window.

```text
Original document
    │
    ├── Chunk 1: Introduction and definitions
    ├── Chunk 2: Eligibility requirements
    ├── Chunk 3: Refund time limits
    └── Chunk 4: Contact information
```

Common chunking choices include:

- Split by paragraphs or document headings when the structure is reliable.
- Split by a fixed number of tokens or characters for plain text.
- Add a small overlap between neighboring chunks so an idea is not cut in half.
- Store the document title and source location with every chunk.

There is no universal best chunk size. Smaller chunks can improve precision; larger chunks can preserve more context. Test with real questions from your users.

## The Complete Architecture

```text
                         INDEXING

Documents → loader → chunks → embedding model → vector store


                     QUESTION ANSWERING

User question → embedding model → retriever → relevant chunks
                                                   │
                                                   ▼
                              prompt with context + question
                                                   │
                                                   ▼
                                                  LLM
                                                   │
                                                   ▼
                                   answer + source citations
```

The vector store helps find relevant information. The LLM then reads that information and creates an answer. Keeping these responsibilities separate makes the system easier to understand and improve.

## A Good RAG Prompt

Retrieved text is not enough by itself. The LLM also needs clear instructions about how to use it.

```text
You are a helpful assistant.

Answer the question using only the context below.
If the context does not contain the answer, say that you do not know.
Include the source name when you use a source.

Context:
{retrieved_chunks}

Question:
{user_question}
```

This instruction reduces unsupported answers, but it does not guarantee accuracy. You should still test the system and show sources to the user.

## Common RAG Problems

| Problem | Likely cause | Improvement |
|---|---|---|
| The answer is unrelated | Retrieval found poor chunks. | Improve chunking, embeddings, metadata, or search settings. |
| The answer misses key information | Too few chunks or chunks are too small. | Retrieve more chunks or increase chunk size and overlap. |
| The answer invents information | The LLM is not constrained enough. | Tell it to use only provided context and return "I don't know" when needed. |
| The answer is too long | Too much context or unclear instructions. | Retrieve fewer, better chunks and request a concise answer. |
| Sources are unclear | Metadata was not stored or displayed. | Store file names, pages, URLs, and chunk identifiers. |
| Old information appears | The index is outdated. | Re-index documents when they change. |

## What We Will Build

Our first example is a small command-line RAG application. It uses:

- `knowledge_base.txt` as the document to search.
- `sentence-transformers/all-MiniLM-L6-v2` to create embeddings and retrieve relevant chunks.
- `HuggingFaceTB/SmolLM2-135M-Instruct` to generate an answer from the retrieved context.

Both models are downloaded from Hugging Face on the first run. After the downloads finish, the application runs locally and does not send the document or question to an API.

The application will:

1. Loads a local text document.
2. Splits it into chunks.
3. Creates embeddings for the chunks.
4. Finds the most relevant chunks for a question.
5. Sends the context and question to an LLM.
6. Displays the answer and the source chunks.

We will start with a simple local document so every step is visible. Later, the same ideas can be used with PDFs, websites, databases, larger vector stores, and a chatbot interface.

## Run the First Local RAG Application

This example requires Python 3.12. On macOS, install it if necessary:

```bash
brew install python@3.12
```

From this folder, create the virtual environment and install the dependencies:

```bash
chmod +x setup_rag.sh
./setup_rag.sh
```

Then activate the environment and start the application:

```bash
source .venv-rag/bin/activate
python rag_app.py
```

On the first run, the embedding model and LLM are downloaded. You can then try questions such as:

```text
What is the refund policy?
When can I contact support?
How do I receive a certificate?
What is the capital of Turkey?
```

The last question is deliberately not in `knowledge_base.txt`. A well-grounded RAG answer should say that it does not know based on the supplied document, instead of answering from general model knowledge.

## Understand the Code

`rag_app.py` has four important stages:

1. **Load and chunk:** `split_into_chunks()` divides `knowledge_base.txt` into smaller sections.
2. **Embed:** `SentenceTransformer` converts every chunk into an embedding, once when the program starts.
3. **Retrieve:** `retrieve()` embeds the user's question and compares it with the stored chunk embeddings. The two highest-scoring chunks become context.
4. **Generate:** `answer_question()` sends the context and question to the local LLM, with instructions not to use information outside that context.

Each answer also prints the retrieved chunks and their similarity scores. This makes it possible to check whether the retriever found the right information before trusting the LLM's answer.

## 📚 References

- [OpenAI: Retrieval guide](https://platform.openai.com/docs/guides/retrieval)
- [Hugging Face: Sentence Transformers](https://www.sbert.net/)
- [FAISS: Similarity search library](https://github.com/facebookresearch/faiss)
