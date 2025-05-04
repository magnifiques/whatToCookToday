import re

def format_recipes(raw_text):
    # Split based on "Title:"
    recipe_chunks = re.split(r'(?=Title:)', raw_text)
    formatted = []

    intro = "👩‍🍳 Here are some delicious recipe suggestions based on your ingredients!\n"
    outro = "\n🍽️ Hope one of these hits the spot!"

    for i, chunk in enumerate(recipe_chunks[:3]):  # Limit to 3 recipes
        if not chunk.strip():
            continue

        # Extract title
        title_match = re.search(r'Title:\s*(.*)', chunk)
        title = title_match.group(1).strip() if title_match else "N/A"

        # Extract ingredients
        ingredients_match = re.search(r'Ingredients:\s*(.*?)(?=\n\w+:|$)', chunk, re.DOTALL)
        ingredients_raw = ingredients_match.group(1).strip() if ingredients_match else "N/A"

        # Capitalize first letter of each word in each ingredient
        ingredients = ", ".join(
            word.strip().title() for word in ingredients_raw.split(",")
        )

        # Extract instructions
        instructions_match = re.search(r'Instructions:\s*(.*?)(?=\n\w+:|$)', chunk, re.DOTALL)
        instructions_raw = instructions_match.group(1).strip() if instructions_match else "N/A"
        
        # Split into lines or sentences while keeping phrases like 'medium-high' intact
        raw_steps = re.split(r'(?<!\w)(?=\n|•|\-|\.)', instructions_raw)
        
        # Clean up each step and remove non-letter characters
        instruction_steps = [step.strip(" -.()") for step in raw_steps if step.strip() and re.search(r'[a-zA-Z]', step)]
        
        # Join together hyphenated words like "medium-high" into one step
        instruction_steps = [re.sub(r'(\b\w+-\w+\b)', lambda m: m.group(0), step) for step in instruction_steps]
        
        # Format steps with emoji bullets
        instructions = "\n".join(f"- {step}" for step in instruction_steps)

        # Format the recipe
        formatted.append(f"""🍲 Recipe {i}: {title}

🧂 Ingredients: {ingredients}
        
👨‍🍳 Instructions - Step-by-step to cook it right:\n
{instructions}\n
"""
)

    return f"{intro}\n\n" + "\n\n".join(formatted) + f"\n\n{outro}"
