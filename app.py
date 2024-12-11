import streamlit as st
from src.zk_proof_system import ZKProofSystem, ZKProof
from src.utils import generate_flowchart

# Page configuration
st.set_page_config(
    page_title="Cryptography ZKProof",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.selectbox("Choose an option", ["Home", "Generate Proof", "Learn More"])

# Load custom CSS for animations
with open("assets/animations.css", "r") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# Home Section
if section == "Home":
    st.markdown(
        f"""
        <div class="home-banner">
            <img src="assets/banner.png" class="banner">
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.title("🔒 Zero-Knowledge Proof (ZKP)")
    st.write(
        """
        Zero-Knowledge Proofs allow a prover to demonstrate knowledge of a secret without revealing it. 
        This cryptographic principle is crucial for ensuring privacy and security in applications like authentication, 
        blockchain, and secure computation.
        """
    )
    st.subheader("Key Properties of ZKP:")
    st.markdown(
        """
        - **Completeness**: If the statement is true, the verifier will be convinced.
        - **Soundness**: If the statement is false, the verifier won't be convinced.
        - **Zero-Knowledge**: No additional information about the secret is revealed.
        """
    )
    st.image("assets/flowchart.png", caption="Flowchart of Zero-Knowledge Proof Process")

# Generate Proof Section
elif section == "Generate Proof":
    st.title("Generate a Zero-Knowledge Proof")
    num_values = st.slider("Number of secret values", 2, 5, 3)
    secret_numbers = [st.number_input(f"Secret number {i+1}", 0, 100, 10) for i in range(num_values)]

    if st.button("Generate Proof"):
        proof_system = ZKProofSystem(secret_numbers)
        random_values = proof_system.generate_random_numbers(len(secret_numbers))
        commitment = proof_system.create_commitment(random_values)
        challenge = proof_system.generate_challenge()
        response = proof_system.generate_response(random_values, challenge)
        proof = ZKProof(commitment, challenge, response)
        public_sum = sum(secret_numbers) % proof_system.modulus

        st.header("Generated Proof")
        st.write(f"Public Sum: {public_sum}")
        st.write(f"Commitment: {proof.commitment}")
        st.write(f"Challenge: {proof.challenge}")
        st.write(f"Response: {proof.response}")

        if proof_system.verify_proof(proof, public_sum):
            st.success("Proof is valid!")
        else:
            st.error("Proof is invalid!")

# Learn More Section
elif section == "Learn More":
    st.title("Understanding the Proof Process")
    st.write(
        """
        The zero-knowledge proof in this application involves the following steps:
        """
    )
    st.image("assets/flowchart.png", caption="Zero-Knowledge Proof Process", use_column_width=True)
    st.markdown(
        """
        1. **Commitment Generation**: The prover generates a commitment using a random value.
        2. **Challenge Generation**: The verifier issues a challenge (0 or 1).
        3. **Response Computation**: The prover computes the response based on the challenge.
        4. **Verification**: The verifier checks the proof's validity.
        """
    )
