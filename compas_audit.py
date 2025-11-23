import React, { useState } from 'react';
import { FileText, Code, Brain, Shield, BookOpen } from 'lucide-react';

const AIEthicsAssignment = () => {
  const [activeTab, setActiveTab] = useState('overview');

  const tabs = [
    { id: 'overview', name: 'Overview', icon: BookOpen },
    { id: 'part1', name: 'Part 1: Theory', icon: Brain },
    { id: 'part2', name: 'Part 2: Cases', icon: FileText },
    { id: 'part3', name: 'Part 3: Audit', icon: Code },
    { id: 'part4', name: 'Part 4: Reflection', icon: Shield },
  ];

  const renderContent = () => {
    switch(activeTab) {
      case 'overview':
        return <Overview />;
      case 'part1':
        return <Part1Theory />;
      case 'part2':
        return <Part2Cases />;
      case 'part3':
        return <Part3Audit />;
      case 'part4':
        return <Part4Reflection />;
      default:
        return <Overview />;
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
      <div className="max-w-6xl mx-auto">
        <header className="bg-white rounded-lg shadow-lg p-6 mb-6">
          <h1 className="text-3xl font-bold text-indigo-900 mb-2">
            AI Ethics Assignment
          </h1>
          <p className="text-gray-600">
            Designing Responsible and Fair AI Systems
          </p>
        </header>

        <div className="bg-white rounded-lg shadow-lg overflow-hidden">
          <div className="flex border-b overflow-x-auto">
            {tabs.map((tab) => {
              const Icon = tab.icon;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`flex items-center gap-2 px-6 py-4 font-medium transition-colors whitespace-nowrap ${
                    activeTab === tab.id
                      ? 'bg-indigo-600 text-white'
                      : 'text-gray-600 hover:bg-gray-50'
                  }`}
                >
                  <Icon size={18} />
                  {tab.name}
                </button>
              );
            })}
          </div>

          <div className="p-6">
            {renderContent()}
          </div>
        </div>
      </div>
    </div>
  );
};

const Overview = () => (
  <div className="space-y-6">
    <div className="bg-indigo-50 border-l-4 border-indigo-600 p-4">
      <h2 className="text-xl font-bold text-indigo-900 mb-2">Assignment Structure</h2>
      <p className="text-gray-700">
        This assignment covers theoretical understanding, case study analysis, practical auditing, and ethical reflection on AI systems.
      </p>
    </div>

    <div className="grid md:grid-cols-2 gap-4">
      <div className="bg-white border rounded-lg p-4 shadow">
        <h3 className="font-bold text-lg mb-2 text-gray-800">Deliverables</h3>
        <ul className="space-y-2 text-gray-700">
          <li className="flex items-start gap-2">
            <FileText size={16} className="mt-1 text-indigo-600" />
            <span>PDF with written answers and case analyses</span>
          </li>
          <li className="flex items-start gap-2">
            <Code size={16} className="mt-1 text-indigo-600" />
            <span>Jupyter Notebook with fairness audit code</span>
          </li>
          <li className="flex items-start gap-2">
            <Shield size={16} className="mt-1 text-indigo-600" />
            <span>Bonus: Healthcare AI policy document</span>
          </li>
        </ul>
      </div>

      <div className="bg-white border rounded-lg p-4 shadow">
        <h3 className="font-bold text-lg mb-2 text-gray-800">Tools & Resources</h3>
        <ul className="space-y-2 text-gray-700">
          <li className="flex items-start gap-2">
            <div className="w-2 h-2 bg-indigo-600 rounded-full mt-2"></div>
            <span>AI Fairness 360 (IBM)</span>
          </li>
          <li className="flex items-start gap-2">
            <div className="w-2 h-2 bg-indigo-600 rounded-full mt-2"></div>
            <span>COMPAS Recidivism Dataset</span>
          </li>
          <li className="flex items-start gap-2">
            <div className="w-2 h-2 bg-indigo-600 rounded-full mt-2"></div>
            <span>EU Ethics Guidelines</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
);

const Part1Theory = () => (
  <div className="space-y-6">
    <section className="bg-white border rounded-lg p-5 shadow">
      <h3 className="text-lg font-bold text-indigo-900 mb-3">Q1: Algorithmic Bias</h3>
      <div className="space-y-3 text-gray-700">
        <p className="font-semibold">Definition:</p>
        <p>
          Algorithmic bias refers to systematic and repeatable errors in computer systems that create unfair outcomes, 
          favoring certain groups over others based on characteristics like race, gender, age, or socioeconomic status.
        </p>
        
        <p className="font-semibold mt-4">Example 1: Healthcare Risk Prediction</p>
        <p>
          An algorithm used to identify patients needing extra medical care systematically underestimated the needs of 
          Black patients. The bias arose because the algorithm used healthcare costs as a proxy for health needs, but 
          Black patients historically had less access to healthcare and lower spending despite equivalent illness severity.
        </p>
        
        <p className="font-semibold mt-4">Example 2: Credit Scoring Systems</p>
        <p>
          Machine learning models for credit decisions may discriminate against applicants from certain zip codes or 
          with non-traditional credit histories, perpetuating historical lending discrimination even when race is not 
          explicitly included as a feature.
        </p>
      </div>
    </section>

    <section className="bg-white border rounded-lg p-5 shadow">
      <h3 className="text-lg font-bold text-indigo-900 mb-3">Q2: Transparency vs Explainability</h3>
      <div className="space-y-3 text-gray-700">
        <div className="bg-blue-50 p-4 rounded">
          <p className="font-semibold">Transparency:</p>
          <p>
            Refers to the openness about how an AI system works, including documentation of data sources, model 
            architecture, training procedures, and decision-making processes. It answers what and how the system operates.
          </p>
        </div>
        
        <div className="bg-green-50 p-4 rounded">
          <p className="font-semibold">Explainability:</p>
          <p>
            Refers to the ability to understand why a specific decision was made in human-interpretable terms. 
            It answers why a particular output was produced for a given input.
          </p>
        </div>
        
        <p className="font-semibold mt-4">Why Both Matter:</p>
        <ul className="list-disc pl-6 space-y-2">
          <li><strong>Accountability:</strong> Transparency enables auditing; explainability enables contesting decisions</li>
          <li><strong>Trust:</strong> Users need to understand both the system and individual outcomes</li>
          <li><strong>Debugging:</strong> Transparency helps identify systemic issues; explainability helps fix individual errors</li>
          <li><strong>Compliance:</strong> Regulations like GDPR require both system documentation and explanation of automated decisions</li>
        </ul>
      </div>
    </section>

    <section className="bg-white border rounded-lg p-5 shadow">
      <h3 className="text-lg font-bold text-indigo-900 mb-3">Q3: GDPR Impact on AI Development</h3>
      <div className="space-y-3 text-gray-700">
        <p>
          The General Data Protection Regulation significantly impacts AI development in the EU through several key provisions:
        </p>
        
        <div className="space-y-3 mt-3">
          <div className="border-l-4 border-indigo-500 pl-4">
            <p className="font-semibold">Right to Explanation:</p>
            <p>Individuals have the right to obtain meaningful information about the logic involved in automated decision-making, 
            requiring explainable AI systems.</p>
          </div>
          
          <div className="border-l-4 border-indigo-500 pl-4">
            <p className="font-semibold">Data Minimization:</p>
            <p>AI systems must collect only necessary data, limiting the scope of training datasets and feature engineering.</p>
          </div>
          
          <div className="border-l-4 border-indigo-500 pl-4">
            <p className="font-semibold">Purpose Limitation:</p>
            <p>Data collected for one purpose cannot be repurposed for AI training without explicit consent, restricting data reuse.</p>
          </div>
          
          <div className="border-l-4 border-indigo-500 pl-4">
            <p className="font-semibold">Right to Be Forgotten:</p>
            <p>Requires mechanisms to remove individual data from training sets and potentially retrain models.</p>
          </div>
          
          <div className="border-l-4 border-indigo-500 pl-4">
            <p className="font-semibold">Privacy by Design:</p>
            <p>AI systems must incorporate privacy protections from the outset, including techniques like differential privacy 
            and federated learning.</p>
          </div>
        </div>
      </div>
    </section>

    <section className="bg-white border rounded-lg p-5 shadow">
      <h3 className="text-lg font-bold text-indigo-900 mb-3">Ethical Principles Matching</h3>
      <div className="space-y-3">
        <div className="grid md:grid-cols-2 gap-4">
          <div className="bg-purple-50 p-4 rounded">
            <p className="font-bold text-purple-900">A) Justice → 4</p>
            <p className="text-gray-700">Fair distribution of AI benefits and risks</p>
          </div>
          
          <div className="bg-red-50 p-4 rounded">
            <p className="font-bold text-red-900">B) Non-maleficence → 1</p>
            <p className="text-gray-700">Ensuring AI does not harm individuals or society</p>
          </div>
          
          <div className="bg-blue-50 p-4 rounded">
            <p className="font-bold text-blue-900">C) Autonomy → 2</p>
            <p className="text-gray-700">Respecting users right to control their data and decisions</p>
          </div>
          
          <div className="bg-green-50 p-4 rounded">
            <p className="font-bold text-green-900">D) Sustainability → 3</p>
            <p className="text-gray-700">Designing AI to be environmentally friendly</p>
          </div>
        </div>
      </div>
    </section>
  </div>
);

const Part2Cases = () => (
  <div className="space-y-6">
    <section className="bg-white border rounded-lg p-5 shadow">
      <h3 className="text-xl font-bold text-indigo-900 mb-4">Case 1: Amazon Biased Hiring Tool</h3>
      
      <div className="space-y-4 text-gray-700">
        <div className="bg-red-50 border-l-4 border-red-500 p-4">
          <h4 className="font-bold text-red-900 mb-2">1. Source of Bias</h4>
          <ul className="space-y-2">
            <li><strong>Training Data Bias:</strong> The model was trained on resumes submitted over 10 years, 
            predominantly from male candidates in tech roles.</li>
            <li><strong>Feature Engineering Issues:</strong> The system learned to penalize resumes with gender-related terms.</li>
            <li><strong>Proxy Variables:</strong> Patterns correlated with gender became implicit indicators.</li>
          </ul>
        </div>

        <div className="bg-green-50 border-l-4 border-green-500 p-4">
          <h4 className="font-bold text-green-900 mb-2">2. Three Fixes for Fairness</h4>
          <div className="space-y-3">
            <div>
              <p className="font-semibold">Fix 1: Balanced Training Data</p>
              <p>Collect and curate a balanced dataset with equal representation of successful candidates across genders. 
              Use techniques like stratified sampling and reweighting.</p>
            </div>
            
            <div>
              <p className="font-semibold">Fix 2: Remove Gender-Correlated Features</p>
              <p>Conduct feature importance analysis to identify and remove features that serve as proxies for gender. 
              Implement adversarial debiasing techniques.</p>
            </div>
            
            <div>
              <p className="font-semibold">Fix 3: Fairness Constraints During Training</p>
              <p>Implement algorithmic fairness constraints like demographic parity or equalized odds during model training 
              using AI Fairness 360 techniques.</p>
            </div>
          </div>
        </div>

        <div className="bg-blue-50 border-l-4 border-blue-500 p-4">
          <h4 className="font-bold text-blue-900 mb-2">3. Fairness Evaluation Metrics</h4>
          <ul className="space-y-2">
            <li><strong>Demographic Parity:</strong> Selection rates should be similar across genders</li>
            <li><strong>Equal Opportunity:</strong> True Positive Rate parity for qualified candidates</li>
            <li><strong>Equalized Odds:</strong> Both TPR and FPR should be equal across groups</li>
            <li><strong>Disparate Impact Ratio:</strong> Ratio of selection rates should be greater than 0.8</li>
            <li><strong>Calibration:</strong> Predicted probabilities should match actual outcomes equally</li>
          </ul>
        </div>
      </div>
    </section>

    <section className="bg-white border rounded-lg p-5 shadow">
      <h3 className="text-xl font-bold text-indigo-900 mb-4">Case 2: Facial Recognition in Policing</h3>
      
      <div className="space-y-4 text-gray-700">
        <div className="bg-red-50 border-l-4 border-red-500 p-4">
          <h4 className="font-bold text-red-900 mb-2">1. Ethical Risks</h4>
          <div className="space-y-3">
            <div>
              <p className="font-semibold">Wrongful Arrests</p>
              <p>Higher false positive rates for minorities lead to wrongful detentions and investigations, 
              disproportionately affecting Black individuals.</p>
            </div>
            
            <div>
              <p className="font-semibold">Privacy and Surveillance</p>
              <p>Mass surveillance capabilities enable tracking individuals without consent, creating a chilling 
              effect on freedom of assembly and protest.</p>
            </div>
            
            <div>
              <p className="font-semibold">Systemic Discrimination</p>
              <p>Biased technology amplifies existing racial disparities in policing, creating feedback loops 
              that reinforce discrimination.</p>
            </div>
            
            <div>
              <p className="font-semibold">Erosion of Trust</p>
              <p>Deployment of biased technology damages community-police relations and undermines trust in 
              law enforcement.</p>
            </div>
          </div>
        </div>

        <div className="bg-green-50 border-l-4 border-green-500 p-4">
          <h4 className="font-bold text-green-900 mb-2">2. Responsible Deployment Policies</h4>
          <div className="space-y-3">
            <div>
              <p className="font-semibold">Mandatory Independent Auditing</p>
              <p>Require third-party testing for accuracy across demographic groups before procurement. 
              Establish minimum accuracy thresholds with less than 1% disparity across races.</p>
            </div>
            
            <div>
              <p className="font-semibold">Human-in-the-Loop Requirements</p>
              <p>Facial recognition should only provide investigative leads, never serve as sole basis for arrest. 
              Require human verification and additional corroborating evidence.</p>
            </div>
            
            <div>
              <p className="font-semibold">Transparency and Public Oversight</p>
              <p>Public disclosure of when and how facial recognition is used, with community input in deployment 
              decisions and civilian oversight boards.</p>
            </div>
            
            <div>
              <p className="font-semibold">Limited Scope and Purpose</p>
              <p>Restrict use to serious crimes only, prohibit real-time surveillance at protests, 
              and implement strict data retention limits.</p>
            </div>
            
            <div>
              <p className="font-semibold">Accountability Mechanisms</p>
              <p>Create clear liability frameworks for wrongful identifications, mandatory reporting of false matches, 
              and independent review of all cases.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
);

const Part3Audit = () => (
  <div className="space-y-6">
    <div className="bg-indigo-50 border-l-4 border-indigo-600 p-4">
      <h3 className="text-lg font-bold text-indigo-900 mb-2">COMPAS Fairness Audit</h3>
      <p className="text-gray-700">
        This section provides the complete code for auditing the COMPAS Recidivism Dataset using AI Fairness 360.
        The code analyzes racial bias in risk scores and generates visualizations.
      </p>
    </div>

    <div className="bg-white border rounded-lg p-5 shadow">
      <h4 className="font-bold text-gray-800 mb-3">Code Implementation Guide</h4>
      <div className="bg-gray-50 p-4 rounded font-mono text-sm">
        <p className="text-gray-600 mb-2"># Download the Python code from the artifact</p>
        <p className="text-gray-600"># Or copy the code provided separately</p>
      </div>
    </div>

    <div className="bg-white border rounded-lg p-5 shadow">
      <h4 className="font-bold text-gray-800 mb-3">Key Analysis Components</h4>
      <div className="space-y-3 text-gray-700">
        <div className="border-l-4 border-blue-500 pl-4">
          <p className="font-semibold">1. Data Loading & Preprocessing</p>
          <p>Load COMPAS dataset and prepare for fairness analysis</p>
        </div>
        <div className="border-l-4 border-green-500 pl-4">
          <p className="font-semibold">2. Bias Metrics Calculation</p>
          <p>Compute disparate impact, statistical parity difference, equal opportunity difference</p>
        </div>
        <div className="border-l-4 border-purple-500 pl-4">
          <p className="font-semibold">3. Visualizations</p>
          <p>Generate charts showing false positive rates, risk score distributions by race</p>
        </div>
        <div className="border-l-4 border-red-500 pl-4">
          <p className="font-semibold">4. Mitigation Strategies</p>
          <p>Apply reweighing and prejudice remover techniques</p>
        </div>
      </div>
    </div>

    <div className="bg-yellow-50 border-l-4 border-yellow-500 p-4">
      <h4 className="font-bold text-yellow-900 mb-2">Expected Findings</h4>
      <p className="text-gray-700">
        The COMPAS audit typically reveals significant racial disparities with Black defendants receiving higher 
        risk scores and experiencing higher false positive rates compared to White defendants, even when controlling 
        for actual recidivism rates.
      </p>
    </div>
  </div>
);

const Part4Reflection = () => (
  <div className="space-y-6">
    <section className="bg-white border rounded-lg p-5 shadow">
      <h3 className="text-xl font-bold text-indigo-900 mb-4">Ethical Reflection on Personal Projects</h3>
      
      <div className="bg-blue-50 border-l-4 border-blue-600 p-4 mb-4">
        <p className="text-gray-700 italic">
          Reflect on a personal project (past or future). How will you ensure it adheres to ethical AI principles?
        </p>
      </div>

      <div className="space-y-4 text-gray-700">
        <div>
          <h4 className="font-bold text-lg mb-2">Project Context</h4>
          <p>
            Consider a student loan approval system that uses machine learning to predict default risk 
            and recommend approval decisions. This touches on critical ethical considerations around fairness, 
            transparency, and social impact.
          </p>
        </div>

        <div className="bg-green-50 p-4 rounded">
          <h4 className="font-bold text-green-900 mb-3">Ethical Principles Implementation</h4>
          
          <div className="space-y-3">
            <div>
              <p className="font-semibold">1. Justice & Fairness</p>
              <ul className="list-disc pl-6 mt-1 space-y-1">
                <li>Conduct pre-deployment bias audits across demographics</li>
                <li>Implement fairness constraints ensuring demographic parity</li>
                <li>Regular monitoring for disparate impact</li>
                <li>Include diverse stakeholders in design</li>
              </ul>
            </div>

            <div>
              <p className="font-semibold">2. Transparency & Explainability</p>
              <ul className="list-disc pl-6 mt-1 space-y-1">
                <li>Document all data sources and model architecture</li>
                <li>Provide clear explanations using LIME or SHAP</li>
                <li>Disclose use of automated decision-making</li>
                <li>Publish model cards with performance metrics</li>
              </ul>
            </div>

            <div>
              <p className="font-semibold">3. Privacy & Autonomy</p>
              <ul className="list-disc pl-6 mt-1 space-y-1">
                <li>Obtain explicit consent for data use</li>
                <li>Implement data minimization principles</li>
                <li>Provide opt-out mechanisms</li>
                <li>Ensure GDPR compliance</li>
              </ul>
            </div>

            <div>
              <p className="font-semibold">4. Non-maleficence</p>
              <ul className="list-disc pl-6 mt-1 space-y-1">
                <li>Conduct impact assessments to identify harms</li>
                <li>Implement human oversight for edge cases</li>
                <li>Create feedback mechanisms</li>
                <li>Regular audits to detect model drift</li>
              </ul>
            </div>

            <div>
              <p className="font-semibold">5. Accountability</p>
              <ul className="list-disc pl-6 mt-1 space-y-1">
                <li>Establish clear ownership and responsibility</li>
                <li>Create audit trails for all decisions</li>
                <li>Form ethics review board</li>
                <li>Develop incident response procedures</li>
              </ul>
            </div>
          </div>
        </div>

        <div className="bg-purple-50 p-4 rounded">
          <h4 className="font-bold text-purple-900 mb-2">Success Metrics</h4>
          <ul className="list-disc pl-6 space-y-1">
            <li>Disparate impact ratio greater than 0.8 across all groups</li>
            <li>90% of applicants understand decision explanations</li>
            <li>Zero successful appeals citing discrimination</li>
            <li>Model performance within 5% across demographics</li>
          </ul>
        </div>
      </div>
    </section>
  </div>
);

export default AIEthicsAssignment;
