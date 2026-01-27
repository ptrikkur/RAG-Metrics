import { Heading, Section } from '@carbon/react';

const Home = () => {
  return (
    <Section>
      <Heading>Welcome to RAG Metrics Calculator</Heading>
      <p style={{ marginTop: '1rem' }}>
        Upload your CSV file containing RAG evaluation data to calculate performance metrics.
      </p>
      <p style={{ marginTop: '0.5rem', color: '#525252' }}>
        Coming soon: File upload and metrics calculation functionality.
      </p>
    </Section>
  );
};

export default Home;

// Made with Bob
