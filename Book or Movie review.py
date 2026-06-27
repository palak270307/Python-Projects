print("🎭 Welcome to Review Hub 🎭")
print("1. Review a Book:")
print("2. Review a Movie:")
choice = input("Choose an option (1 or 2): ")

match choice:
	case "1":
		print("You chose to review a Book.")
		print("Select a genre:")
		print("1. Fiction\n 2. Mystery\n 3. Horror\n 4. Romance\n 5. Science fiction\n 6. History")
		genre = input("Enter the number corresponding to your genre: ")
		
		match genre:
			case "1":
				genre_name = "Fiction"
				print("You selected Fiction.")
			case "2":
				genre_name = "Mystery"
				print("You selected Mystery.")
			case "3":
				genre_name = "Horror"
				print("You selected Horror.")
			case "4":
				genre_name = "Romance"
				print("You selected Romance.")
			case "5":
				genre_name = "Science fiction"
				print("You selected Science fiction.")
			case "6":
				genre_name = "History"
				print("You selected History.")
			case _:
				print(" ❌ Invalid genre selected.")
				exit()


review = input(f"\nWrite your {genre_name} book review: ")
rating = float(input("Rate it out of 5: "))
print(f"\nThank you for your review of the {genre_name} book!")

print("\n📘 Your Book Review Summary 📘")
print(f"Genre: {genre_name}")
print(f"Review: {review}")
print(f"Rating: {rating}/5")

match choice:
	case "2":
		print("You chose to review a Movie.")
		print("Select a genre:")
		print("1. Action\n 2. Comedy\n 3. Drama\n 4. Horror\n 5. Science fiction\n 6. Documentary")
		genre = input("Enter the number corresponding to your genre: ")
		
		match genre:
			case "1":
				genre_name = "Action"
				print("You selected Action.")
			case "2":
				genre_name = "Comedy"
				print("You selected Comedy.")
			case "3":
				genre_name = "Drama"
				print("You selected Drama.")
			case "4":
				genre_name = "Horror"
				print("You selected Horror.")
			case "5":
				genre_name = "Science fiction"
				print("You selected Science fiction.")
			case "6":
				genre_name = "Documentary"
				print("You selected Documentary.")
			case _:
				print(" ❌ Invalid genre selected.")
				exit()


review = input(f"\nWrite your {genre_name} Movie review: ")
rating = float(input("Rate it out of 5: "))
print(f"\nThank you for your review of the {genre_name} Movie!")

print("\n📘 Your Movie Review Summary 📘")
print(f"Genre: {genre_name}")
print(f"Review: {review}")
print(f"Rating: {rating}/5")




























