import streamlit as st
from collections import Counter
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

# --- DNA Analyzer Class ---
class DNAAnalyzer:
    def __init__(self, sequence):
        self.sequence = sequence.strip().replace("\n", "").upper()

    def is_valid(self):
        return all(base in "ATCG" for base in self.sequence)

    def length(self):
        return len(self.sequence)

    def gc_content(self):
        g = self.sequence.count("G")
        c = self.sequence.count("C")
        return round(((g + c) / len(self.sequence)) * 100, 2) if self.sequence else 0

    def find_start_codons(self):
        return [i for i in range(0, len(self.sequence) - 2, 3) if self.sequence[i:i+3] == "ATG"]

    def find_stop_codons(self):
        return [(self.sequence[i:i+3], i) for i in range(0, len(self.sequence) - 2, 3)
                if self.sequence[i:i+3] in ["TAA", "TAG", "TGA"]]

    def codon_frequency(self):
        codons = [self.sequence[i:i+3] for i in range(0, len(self.sequence) - 2, 3)]
        return Counter(codons)

# --- PDF Export Function ---
def generate_pdf(analysis_results):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica", 12)
    width, height = letter

    # Title
    c.drawString(100, height - 40, "🧬 DNA Analysis Report")

    # Analysis Results
    y_position = height - 60
    for line in analysis_results:
        c.drawString(100, y_position, line)
        y_position -= 20

    # Save the PDF to buffer
    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer

# --- Streamlit App ---
def main():
    st.title("🧬 DNA Pattern Analyzer & Visualizer (OOP Streamlit)")

    st.write("Enter your DNA sequence below (A, T, C, G only):")
    sequence_input = st.text_area("DNA Sequence", height=200)

    if st.button("🔍 Analyze DNA"):
        analyzer = DNAAnalyzer(sequence_input)

        if not analyzer.is_valid():
            st.error("Invalid DNA sequence! Please enter only A, T, C, G.")
            return

        st.success("DNA analysis completed successfully!")

        # Store the analysis results
        analysis_results = [
            f"*Length:* {analyzer.length()} bases",
            f"*GC Content:* {analyzer.gc_content()} %",
            f"*Start Codon Positions (ATG):* {analyzer.find_start_codons()}",
            f"*Stop Codons (TAA, TAG, TGA):* {analyzer.find_stop_codons()}"
        ]

        st.markdown("### 🧪 Analysis Results")
        for result in analysis_results:
            st.write(result)

        st.markdown("### 📊 Codon Frequencies")
        freq = analyzer.codon_frequency()
        if freq:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.bar(freq.keys(), freq.values(), color='mediumseagreen')
            ax.set_title("Codon Frequency")
            ax.set_xlabel("Codon")
            ax.set_ylabel("Count")
            st.pyplot(fig)
        else:
            st.warning("No codons found to plot.")

        # Provide an option to download PDF
        if st.button("Download as PDF"):
            pdf_buffer = generate_pdf(analysis_results)
            st.download_button(
                label="Download PDF",
                data=pdf_buffer,
                file_name="dna_analysis_report.pdf",
                mime="application/pdf"
            )

if __name__ == "__main__":
    main()
st.write("Made with ❤️ by [Tehreem Abdullah]")