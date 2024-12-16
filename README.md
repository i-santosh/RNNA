# RNNA
A Recursive Neural Network Algorithm for Compression

# Neuralize Encoding and Decoding System

## Overview

The Neuralize system is a custom text encoding and decoding mechanism that provides a unique way of transforming text through a positional character encoding algorithm. It offers a novel approach to text transformation that maintains the original text's character composition while generating a complex encoding key.

## Key Components

### Functions

#### `neuralize(data: str) -> str`
Encodes input text into a specialized cypher string.

**Parameters:**
- `data`: Input text to be encoded

**Returns:**
- A cypher string in the format: `"data_length..key..unique_characters"`

#### `deneuralize(cypher: str) -> str`
Decodes the cypher string back to the original text.

**Parameters:**
- `cypher`: Encoded cypher string to be decoded

**Returns:**
- Reconstructed original text

## Encoding Process

### Unique Character Extraction
1. Extracts unique characters from the input text
2. Preserves the original order of characters
3. Creates a `nodes` list of unique characters

### Key Generation
- Starts with an initial key value of 1
- Iteratively modifies the key based on:
  - Number of unique characters
  - Position of characters in the input text
- Uses a complex calculation: 
  `key = key * len(nodes) - (len(nodes) - (nodes.index(char) + 1))`

### Cypher Creation
Combines three elements into a single string:
1. Length of original input text
2. Generated encryption key
3. Unique characters used in the text

## Decoding Process

### Cypher Parsing
1. Splits the cypher string into:
   - Data length
   - Encryption key
   - Unique character nodes

### Text Reconstruction
- Uses the key and unique characters to progressively rebuild the text
- Calculates character positions through a range-based algorithm
- Ensures exact reconstruction of the original text

## Example Usage

```python
# Encoding
original_text = "The kernel serves as core operating system component that manages hardware resources."
cypher = neuralize(original_text)
print(cypher)

# Decoding
reconstructed_text = deneuralize(cypher)
print(reconstructed_text)
```

## Characteristics

### Strengths
- Preserves original text characters
- Uses a unique positional encoding method
- Generates a complex, position-dependent key

### Limitations
- Not a cryptographically secure encryption method
- Performance may degrade with very long input texts
- Designed for experimental/educational purposes

## Theoretical Insights

The algorithm demonstrates a novel approach to text transformation by:
- Treating text as a sequence of unique positional elements
- Creating a key that depends on both character composition and position
- Providing a deterministic encoding and decoding mechanism

## Potential Applications

- Educational demonstrations of encoding concepts
- Custom text obfuscation
- Experimental character transformation techniques

## Caution

🚨 **Important:** This is not a secure encryption method and should not be used for sensitive data protection. Always use standard, well-vetted cryptographic libraries for secure communications.

## Performance Considerations

- Time complexity: O(n), where n is the length of the input text
- Space complexity: O(m), where m is the number of unique characters

## Future Improvements

Potential areas for enhancement:
- Add support for international character sets
- Implement more complex key generation algorithms
- Create variations with different encoding strategies

## Mathematical Foundations

The encoding relies on:
- Unique character set manipulation
- Positional encoding principles
- Modular arithmetic for key generation

## License

This code is provided for educational and experimental purposes. Use at your own discretion.
