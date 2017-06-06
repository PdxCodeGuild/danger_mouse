import mouse_game


horace = mouse_game.Mouse("Rasputin", "A wise mouse.", ["befriend"])
# bread = mouse_game.Food(name="bread", score=20)
spell = mouse_game.Spell("hide")

print(horace.take_spell(spell))


