import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import json
import re
from datetime import datetime
from typing import Dict, List, Tuple
import difflib

class CommunityResourceNavigator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI Community Resource Navigator")
        self.root.geometry("1000x700")
        
        self.resources = {
            "healthcare": [
                {
                    "name": "Community Health Center",
                    "type": "Primary Care",
                    "description": "Sliding scale fees based on income. Comprehensive healthcare including mental health services.",
                    "contact": "555-0101",
                    "address": "123 Health St",
                    "eligibility": "All income levels accepted",
                    "keywords": ["doctor", "medical", "checkup", "illness", "mental health", "therapy"]
                },
                {
                    "name": "Free Dental Clinic",
                    "type": "Dental Care",
                    "description": "Free dental services for low-income individuals and families.",
                    "contact": "555-0102",
                    "address": "456 Smile Ave",
                    "eligibility": "Income below 200% federal poverty level",
                    "keywords": ["teeth", "dental", "cavity", "cleaning", "oral health"]
                }
            ],
            "housing": [
                {
                    "name": "Emergency Housing Program",
                    "type": "Emergency Shelter",
                    "description": "Temporary housing assistance and case management services.",
                    "contact": "555-0201",
                    "address": "789 Shelter Rd",
                    "eligibility": "Individuals and families experiencing homelessness",
                    "keywords": ["homeless", "shelter", "emergency housing", "temporary"]
                },
                {
                    "name": "Rent Assistance Program",
                    "type": "Financial Assistance",
                    "description": "Rental assistance and utility payments for qualifying households.",
                    "contact": "555-0202",
                    "address": "321 Support St",
                    "eligibility": "Income below 80% area median income",
                    "keywords": ["rent", "eviction", "utility", "financial help"]
                }
            ],
            "food": [
                {
                    "name": "Community Food Bank",
                    "type": "Food Assistance",
                    "description": "Free groceries and hot meals. No documentation required.",
                    "contact": "555-0301",
                    "address": "654 Food Way",
                    "eligibility": "Open to all in need",
                    "keywords": ["hungry", "food", "groceries", "meals", "pantry"]
                },
                {
                    "name": "Senior Nutrition Program",
                    "type": "Meal Delivery",
                    "description": "Home-delivered meals for seniors and disabled individuals.",
                    "contact": "555-0302",
                    "address": "987 Elder St",
                    "eligibility": "Age 60+ or disabled",
                    "keywords": ["senior", "elderly", "meal delivery", "disabled", "nutrition"]
                }
            ],
            "legal": [
                {
                    "name": "Legal Aid Society",
                    "type": "Legal Services",
                    "description": "Free legal assistance for civil matters including housing, family, and immigration law.",
                    "contact": "555-0401",
                    "address": "147 Justice Ave",
                    "eligibility": "Income below 125% federal poverty level",
                    "keywords": ["lawyer", "legal help", "court", "immigration", "family law", "tenant rights"]
                },
                {
                    "name": "Victim Rights Center",
                    "type": "Legal Advocacy",
                    "description": "Legal advocacy and support services for crime victims.",
                    "contact": "555-0402",
                    "address": "258 Safety Blvd",
                    "eligibility": "Crime victims and their families",
                    "keywords": ["victim", "crime", "advocacy", "restraining order", "support"]
                }
            ],
            "employment": [
                {
                    "name": "Job Training Center",
                    "type": "Workforce Development",
                    "description": "Free job training, resume assistance, and placement services.",
                    "contact": "555-0501",
                    "address": "369 Career St",
                    "eligibility": "Adults seeking employment",
                    "keywords": ["job", "employment", "training", "resume", "career", "work"]
                },
                {
                    "name": "Small Business Development",
                    "type": "Business Support",
                    "description": "Free consulting and resources for starting or growing a small business.",
                    "contact": "555-0502",
                    "address": "741 Enterprise Way",
                    "eligibility": "Prospective and existing small business owners",
                    "keywords": ["business", "entrepreneur", "startup", "consulting", "loan"]
                }
            ],
            "education": [
                {
                    "name": "Adult Learning Center",
                    "type": "Education Services",
                    "description": "GED preparation, ESL classes, and basic computer skills training.",
                    "contact": "555-0601",
                    "address": "852 Learning Ln",
                    "eligibility": "Adults 18 and older",
                    "keywords": ["GED", "education", "ESL", "English", "computer skills", "learning"]
                },
                {
                    "name": "Children's Tutoring Program",
                    "type": "Youth Services",
                    "description": "Free after-school tutoring and homework help for K-12 students.",
                    "contact": "555-0602",
                    "address": "963 Study St",
                    "eligibility": "Students K-12 from low-income families",
                    "keywords": ["tutoring", "homework", "children", "student", "school", "academic"]
                }
            ],
            "mental_health": [
                {
                    "name": "Crisis Intervention Center",
                    "type": "Mental Health",
                    "description": "24/7 crisis counseling and suicide prevention services.",
                    "contact": "555-0701 (24/7 hotline)",
                    "address": "741 Hope Ave",
                    "eligibility": "Open to all",
                    "keywords": ["crisis", "suicide", "depression", "anxiety", "mental health", "counseling"]
                },
                {
                    "name": "Community Counseling Center",
                    "type": "Therapy Services",
                    "description": "Individual, family, and group therapy with sliding scale fees.",
                    "contact": "555-0702",
                    "address": "852 Wellness Way",
                    "eligibility": "All income levels, sliding scale available",
                    "keywords": ["therapy", "counseling", "family", "trauma", "addiction", "support group"]
                }
            ]
        }
        
        self.setup_gui()
        
    def setup_gui(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)

        title_label = ttk.Label(main_frame, text="AI Community Resource Navigator", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        instructions = ttk.Label(main_frame, 
                               text="Describe your situation or what kind of help you need. Our AI will find matching resources.",
                               wraplength=800)
        instructions.grid(row=1, column=0, columnspan=3, pady=(0, 10))
        
        input_frame = ttk.LabelFrame(main_frame, text="Tell us about your needs:", padding="10")
        input_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(0, weight=1)
        
        self.input_text = scrolledtext.ScrolledText(input_frame, height=4, wrap=tk.WORD)
        self.input_text.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        examples_label = ttk.Label(input_frame, text="Examples:")
        examples_label.grid(row=1, column=0, sticky=tk.W)
        
        example_texts = [
            "I need help with rent payment",
            "Looking for free dental care",
            "My child needs tutoring help",
            "I'm struggling with depression",
            "Need job training programs"
        ]
        
        for i, example in enumerate(example_texts):
            btn = ttk.Button(input_frame, text=example, 
                           command=lambda e=example: self.set_example_text(e))
            btn.grid(row=2 + i//3, column=i%3, padx=5, pady=2, sticky=tk.W)
        
        search_btn = ttk.Button(input_frame, text="Find Resources", 
                              command=self.find_resources, style="Accent.TButton")
        search_btn.grid(row=4, column=1, pady=10, sticky=tk.E)
        
        results_frame = ttk.LabelFrame(main_frame, text="Recommended Resources:", padding="10")
        results_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        
        self.results_text = scrolledtext.ScrolledText(results_frame, height=20, wrap=tk.WORD)
        self.results_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.results_text.tag_configure("header", font=('Arial', 12, 'bold'), foreground='blue')
        self.results_text.tag_configure("subheader", font=('Arial', 10, 'bold'))
        self.results_text.tag_configure("contact", font=('Arial', 10, 'bold'), foreground='green')
        
    def set_example_text(self, text):
        """Set example text in the input field"""
        self.input_text.delete(1.0, tk.END)
        self.input_text.insert(1.0, text)
        
    def analyze_needs(self, user_input: str) -> List[Tuple[str, Dict, float]]:
        user_input_lower = user_input.lower()
        matches = []
        
        user_words = re.findall(r'\b\w+\b', user_input_lower)
        
        for category, resources in self.resources.items():
            for resource in resources:
                confidence = 0
              
                keyword_matches = sum(1 for keyword in resource['keywords'] 
                                    if any(difflib.SequenceMatcher(None, keyword, word).ratio() > 0.8 
                                          for word in user_words))
                confidence += keyword_matches * 20
                
                if self.analyze_context(user_input_lower, category, resource):
                    confidence += 30
                
                desc_similarity = difflib.SequenceMatcher(None, user_input_lower, 
                                                        resource['description'].lower()).ratio()
                confidence += desc_similarity * 25
                
                urgency_keywords = ['emergency', 'urgent', 'crisis', 'immediate', 'now', 'help']
                if any(word in user_input_lower for word in urgency_keywords):
                    if 'emergency' in resource['type'].lower() or 'crisis' in resource['name'].lower():
                        confidence += 40
                
                if confidence > 25:
                    matches.append((category, resource, min(confidence, 100)))
        
        return sorted(matches, key=lambda x: x[2], reverse=True)
    
    def analyze_context(self, user_input: str, category: str, resource: Dict) -> bool:
    
        context_patterns = {
            'healthcare': ['sick', 'pain', 'doctor', 'medicine', 'health', 'medical'],
            'housing': ['homeless', 'eviction', 'rent', 'housing', 'apartment', 'shelter'],
            'food': ['hungry', 'food', 'eat', 'meal', 'groceries', 'pantry'],
            'legal': ['court', 'legal', 'lawyer', 'rights', 'law', 'justice'],
            'employment': ['job', 'work', 'unemployed', 'career', 'employment'],
            'education': ['school', 'learn', 'education', 'study', 'class'],
            'mental_health': ['depressed', 'anxious', 'stressed', 'mental', 'therapy']
        }
        
        if category in context_patterns:
            return any(pattern in user_input for pattern in context_patterns[category])
        return False
    
    def find_resources(self):
        user_input = self.input_text.get(1.0, tk.END).strip()
        
        if not user_input:
            messagebox.showwarning("Input Required", "Please describe your needs first.")
            return
        
        self.results_text.delete(1.0, tk.END)
        
        matches = self.analyze_needs(user_input)
        
        if not matches:
            self.results_text.insert(tk.END, "No specific matches found. Here are some general resources:\n\n")
            general_resources = [
                ("healthcare", self.resources["healthcare"][0]),
                ("legal", self.resources["legal"][0]),
                ("food", self.resources["food"][0])
            ]
            for category, resource in general_resources:
                self.display_resource(category, resource, 50)
        else:

            self.results_text.insert(tk.END, "🤖 AI Analysis Summary:\n", "header")
            self.results_text.insert(tk.END, f"Based on your description, I found {len(matches)} relevant resources. ")
            self.results_text.insert(tk.END, f"Here are the best matches ranked by relevance:\n\n")
            
        
            for i, (category, resource, confidence) in enumerate(matches[:8]):  
                self.display_resource(category, resource, confidence, rank=i+1)
    
    def display_resource(self, category: str, resource: Dict, confidence: float, rank: int = None):
   
        if rank:
            self.results_text.insert(tk.END, f"#{rank} ", "header")
        
        self.results_text.insert(tk.END, f"{resource['name']}\n", "header")
        self.results_text.insert(tk.END, f"Category: {category.replace('_', ' ').title()} | ", "subheader")
        self.results_text.insert(tk.END, f"Type: {resource['type']} | ", "subheader")
        self.results_text.insert(tk.END, f"Match: {confidence:.0f}%\n", "subheader")
        
        self.results_text.insert(tk.END, f"\nDescription: {resource['description']}\n")
        self.results_text.insert(tk.END, f"📞 Contact: {resource['contact']}\n", "contact")
        self.results_text.insert(tk.END, f"📍 Address: {resource['address']}\n")
        self.results_text.insert(tk.END, f"✅ Eligibility: {resource['eligibility']}\n")
        
        self.results_text.insert(tk.END, "\n💡 Next Steps: ")
        if 'crisis' in resource['name'].lower() or 'emergency' in resource['type'].lower():
            self.results_text.insert(tk.END, "This is an emergency service. Call immediately if you need urgent help.")
        else:
            self.results_text.insert(tk.END, "Call to verify eligibility and schedule an appointment or visit.")
        
        self.results_text.insert(tk.END, "\n" + "="*80 + "\n\n")
    
    def run(self):
  
        # Add some styling
        style = ttk.Style()
        style.configure("Accent.TButton", font=('Arial', 10, 'bold'))
        
        # Show welcome message
        welcome_msg = """Welcome to the AI Community Resource Navigator!

        self.results_text.insert(tk.END, welcome_msg)
        
        self.root.mainloop()

def main():
    """Main function to run the application"""
    app = CommunityResourceNavigator()
    app.run()

if __name__ == "__main__":
    main()
