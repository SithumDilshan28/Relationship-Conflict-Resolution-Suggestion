import streamlit as st

# Set page configuration
st.set_page_config(page_title="Relationship Advice", layout="wide", page_icon="💬")

# Title of the web app
st.title("💬 Relationship Advice Suggestion App")

# Relationship problems data with problems added to keywords
problems_data = [
    {
        "problem": "My partner doesn't listen when I express how I feel. They always change the subject.",
        "keywords": [
            "communication", "emotional neglect", "active listening", "validation", "empathy", "defensiveness",
            "my partner doesn't listen when I express how I feel", "they always change the subject"
        ],
        "advanced_suggestion": (
            "To foster healthy communication, it's essential to practice active listening. Both partners should focus "
            "on understanding each other’s perspective before responding. One method to encourage better communication is "
            "using reflective listening, where you repeat what your partner says to show understanding and prevent miscommunication. "
            "When expressing your feelings, avoid accusatory language, as it can trigger defensiveness. Instead, focus on using 'I feel' statements. "
            "Also, agree on a time to talk where both of you are mentally present. If your partner struggles with listening, suggest breaks between conversations "
            "to allow each of you to process and reflect. Communication is a two-way street that involves empathy, validation, and emotional support."
        ),
    },
    {
        "problem": "We often argue about how much time we spend with each other. I feel neglected.",
        "keywords": [
            "time management", "emotional intimacy", "quality time", "neglect", "personal space", "balance",
            "we often argue about how much time we spend with each other", "i feel neglected"
        ],
        "advanced_suggestion": (
            "Relationship satisfaction often hinges on how well couples balance quality time and personal space. Create a plan that sets aside specific times during the week for 'couple activities.' "
            "This could involve shared hobbies, dinner without distractions, or even quiet time spent together, allowing for emotional intimacy to grow. Additionally, it's crucial to understand and respect "
            "each other's needs for alone time. If your partner enjoys their personal space, recognize that time apart can help strengthen the relationship by giving each person a chance to recharge. "
            "When communicating about this issue, express that feeling neglected isn’t about clinginess but about maintaining an emotional connection."
        ),
    },
    {
        "problem": "My partner hides things from me, like small purchases or where they've been.",
        "keywords": [
            "trust", "transparency", "secrecy", "financial honesty", "insecurity", "fear of conflict",
            "my partner hides things from me", "small purchases", "where they've been"
        ],
        "advanced_suggestion": (
            "Building a foundation of trust is vital for any relationship, and secrecy, even about small things, can create long-term damage. Rather than accusing your partner of dishonesty, "
            "open a conversation about why they feel the need to hide things. Often, hidden behavior stems from a fear of conflict or disappointing the other person. Ensure that your partner feels safe being "
            "transparent by creating a non-judgmental environment where both of you can openly discuss concerns without fear of reprimand. Set mutual boundaries for transparency, such as agreeing to talk openly "
            "about finances and whereabouts, which helps foster security and emotional safety in the relationship."
        ),
    },
    {
        "problem": "We keep fighting about our future. I want kids, and they don’t.",
        "keywords": [
            "future planning", "family decisions", "children", "life goals", "compromise", "long-term compatibility",
            "we keep fighting about our future", "i want kids", "they don’t"
        ],
        "advanced_suggestion": (
            "Differences in life goals, such as having children, can be a serious point of contention. First, it’s important to have a deep and honest conversation about why each of you holds the views you do. "
            "Listen to your partner’s reasons for not wanting kids and reflect on your reasons for wanting them. Often, fear, personal experiences, or career aspirations shape these decisions. "
            "To navigate this conflict, it’s crucial to determine whether this issue is negotiable or a deal-breaker for either party. Couples therapy can be extremely helpful for navigating such significant decisions, "
            "especially if compromise seems challenging. Long-term compatibility should be based on shared values and understanding each other's vision for the future."
        ),
    },
    {
        "problem": "My partner is always on their phone when we’re together. It makes me feel unimportant.",
        "keywords": [
            "attention", "distraction", "quality time", "digital boundaries", "technology addiction", "emotional connection",
            "my partner is always on their phone when we’re together", "it makes me feel unimportant"
        ],
        "advanced_suggestion": (
            "In the modern age, technology and screen time can significantly affect emotional connection between partners. If your partner’s phone usage is interfering with your quality time, consider establishing digital boundaries. "
            "Discuss the importance of being fully present with each other and agree on times where phones are set aside, such as during meals or at bedtime. Encourage activities that don’t involve technology to reconnect emotionally. "
            "Additionally, explore whether there’s an underlying reason why your partner may be using their phone more frequently, such as stress or the desire to disconnect. Communication and understanding are key to finding balance between "
            "personal device use and nurturing the relationship."
        ),
    },
    {
        "problem": "We constantly argue about finances, especially regarding savings and spending habits.",
        "keywords": [
            "financial disagreements", "budgeting", "spending habits", "financial planning", "shared goals", "compromise", "money management",
            "we constantly argue about finances", "savings and spending habits"
        ],
        "advanced_suggestion": (
            "Money-related issues are one of the top stressors in relationships. Establishing clear financial goals and aligning your spending habits is essential to reduce conflict. Begin by discussing your financial philosophies—are you a spender or saver? "
            "Acknowledge each other’s financial styles and explore ways to find middle ground. Working together to create a budget can help set mutual boundaries and avoid future arguments. It may also be helpful to set up regular financial check-ins to assess your progress "
            "and adjust your plan as necessary. Remember, financial planning in a relationship should be about teamwork and supporting each other’s long-term financial health, not a battle over control."
        ),
    }
]

# Input from the user
st.subheader("Enter your relationship problem:")
user_problem = st.text_area("Describe your problem here", height=150)

# Process user input
if st.button("Get Advice"):
    if user_problem.strip():
        # Convert user problem to lowercase for case-insensitive matching
        user_problem_lower = user_problem.lower()
        
        # Check for keywords and provide suggestions
        matched_suggestion = None
        matched_problem = None
        
        for problem_data in problems_data:
            # Check if any keyword from the predefined problems or full problem statements is present in the user's input
            if any(keyword.lower() in user_problem_lower for keyword in problem_data['keywords']):
                matched_suggestion = problem_data['advanced_suggestion']
                matched_problem = problem_data['problem']
                break
        
        if matched_suggestion:
            st.markdown("### Matched Problem:")
            st.write(f"**{matched_problem}**")  # Display the matched predefined problem
            st.success("### Advanced Suggestion:")
            st.write(matched_suggestion)  # Display the matched advanced suggestion
        else:
            st.warning("No specific advice was found based on the provided problem. Please try describing your problem with more details or use related keywords.")
    else:
        st.error("Please enter a problem description!")

# Sidebar with additional options
with st.sidebar:
    st.image("expert_banner.png", use_column_width=True)  # You can use a custom image here
    st.header("About")
    st.write(
        """
        This app uses Machine Learning and NLP to recommend experts based on your problem description. 
        Simply describe your issue, and get matched with an expert in Legal, Fitness, Career, Health, Finance, or Relationships.
        """
    )
    st.write("Developed by: U-Connect")



    # Add footer with social media links
st.markdown("---")
st.markdown("💬 Connect with us: [LinkedIn](https://www.linkedin.com/) | [Twitter](https://twitter.com/) | [GitHub](https://github.com/)")
