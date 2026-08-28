
# SweetLab 🍰

ok so this is my python learning project. basically a bakery but make it terminal.

## what's this about

i wanted to actually USE the stuff i learned in python instead of just watching tutorials forever. you know the loop right - watch video, nod, think you got it, next video, repeat. so i made this.

it's a bakery management thingy. you can be a customer and buy cake (well, fake buy) or be an admin and pretend you run a real business. everything saves to a json file so your fake bakery survives restarts.

## features

**customer side:**
- view all products (with prices and stock)
- search for stuff (case insensitive, so "cake" "CAKE" "Cake" all work)
- add things to cart
- remove things from cart
- clear cart when you regret everything
- place order and get an order id

**admin side:**
- view, add, edit, delete products
- search products
- view all orders
- change order status (Pending → Preparing → Completed → Cancelled)
- see stats (total products, orders, inventory value, most ordered item)

**other stuff:**
- single json file holds everything
- stock auto decreases when you add to cart, comes back if you remove
- order ids auto-increment and survive restarts
- a loading screen that says "please wait . . ." because i thought it looked cool
- admin password is 1234 (very secure i know, please don't hack my bakery)

## how to run

yeah that's it. on first run it makes its own `sweetlab_data.json` file with some default products. from then on everything you do gets saved there.

## why did i build this

honestly just to see if i could. the goal wasn't to make a real store, just to actually use the things tutorials showed but i never touched:

- lists, dicts, tuples
- for / while loops
- if / elif / else
- functions (lots of them)
- try / except
- file handling with json
- enumerate (this one's underrated)
- global variables (annoying but sometimes necessary)
- datetime for order timestamps

## stuff i learned

- json is actually way handier than i thought
- global variables are annoying but sometimes you just need them
- try / except saved my life like 100 times
- terminal animations with `time.sleep()` make everything feel more legit
- naming functions is harder than writing them
- reading code from 2 weeks ago feels like reading someone else's code

## known quirks (not bugs, quirks)

- the loading animation is probably longer than it needs to be
- the word "succsefuly" is misspelled on purpose (no it wasn't, but now it stays)
- "loding" instead of "loading" - same energy
- if you type something completely weird the program might yell at you
- admin password is hardcoded, this is not production ready lol

## tech

- python 3
- json for storage
- that's it. no frameworks no libraries no pip install needed

## would i do anything different

probably. but it works and i learned a lot so 🤷

if you're also learning python and want to peek at the code, go for it. just don't judge the parts where i did things the long way on purpose. that was the point.

made with too much coffee and not enough sleep 💀
