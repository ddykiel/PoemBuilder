import f
import line
import pygame

mainloop = True

loop_count = 1

while mainloop:

    line1 = line.line1.copy()
    line2 = line.line2.copy()
    line3 = line.line3.copy()
    line4 = line.line4.copy()
    line5 = line.line5.copy()
    line6 = line.line6.copy()
    line7 = line.line7.copy()
    line8 = line.line8.copy()
    line9 = line.line9.copy()
    line10 = line.line10.copy()
    line11 = line.line11.copy()
    line12 = line.line12.copy()

    choice1 = f.get_choice(line1)

    f.poem_started = True
    if choice1 == line.something_in_voice:
        line2.remove(line.fall_through)
    if choice1 == line.sink_into_skin:
        line2.remove(line.shivers)
        line2.remove(line.tongue_leaden)
        line2.append(line.tongue_leaden_edit)

    choice2 = f.get_choice(line2)

    choice3 = f.get_choice(line3)
    if choice3 == line.wind:
        line4.remove(line.trust_draw_blood)
        line4.remove(line.draw_blood)
    if choice3 == line.rich_exploitation:
        line4.remove(line.cold_and_dead)
        line4.remove(line.trust_draw_blood)
    if choice3 == line.scrape_words:
        line4.remove(line.cold_and_dead)
        line4.remove(line.self_sacrifice)
        line4.remove(line.your_dreams)
    if choice3 == line.planes:
        line4.remove(line.cold_and_dead)
        line4.remove(line.trust_draw_blood)
        line4.remove(line.draw_blood)

    choice4 = f.get_choice(line4)
    if choice4 == line.cold_and_dead:
        line5.remove(line.sickness)
        line5.remove(line.crumbled)
        line5.remove(line.melancholy)
        line5.remove(line.and_comforting)
        line5.remove(line.becomes_comforting)
    if choice4 == line.self_sacrifice:
        line5.remove(line.especially_us)
        line5.remove(line.bury_it)
        line5.remove(line.melancholy)
        line5.remove(line.and_comforting)
    if choice4 == line.trust_draw_blood or choice4 == line.draw_blood:
        line5.clear()
        line5.append(line.sickness)
        line5.append(line.crumbled)
        line5.append(line.becomes_comforting)
    if choice4 == line.your_dreams:
        line5.remove(line.becomes_comforting)
        line5.append(line.becomes_comforting_edit)
        line5.remove(line.sickness)
        line5.append(line.sickness_edit)
        line5.remove(line.especially_us)
        line5.remove(line.bury_it)
        line5.remove(line.crumbled)
        line5.append(line.crumbled_edit)

    choice5 = f.get_choice(line5)

    choice6 = f.get_choice(line6)
    if choice6 != line.forgive_me:
        line7.remove(line.violence)

    choice7 = f.get_choice(line7)
    if choice7 == line.violence:
        line8.remove(line.strained)
        line8.remove(line.church_bells)
    if choice7 == line.intimacies_breathe:
        line8.clear()
        line8.append(line.in_quiet)
        line8.append(line.tenuous_intimacies_edit)
    if choice7 == line.silence_digs:
        line8.remove(line.in_quiet)

    choice8 = f.get_choice(line8)
    if choice8 == line.hollow_essence:
        line9.remove(line.ribs)
        line9.append(line.ribs_edit)
        line9.remove(line.vanity)
    if choice8 == line.words_burn:
        line9.remove(line.cave_shoulders)
        line9.remove(line.impress)
        line9.remove(line.vanity)
    if choice8 == line.drink_air:
        line9.remove(line.scars)
        line9.remove(line.cave_shoulders)
        line9.remove(line.ribs)
    if choice8 == line.your_quiet:
        line9.remove(line.ribs)
    if choice8 == line.in_quiet:
        line9.remove(line.vanity)

    choice9 = f.get_choice(line9)
    if choice9 == line.sour or choice9 == line.scars or choice9 == line.thick_cloying:
        line10.remove(line.soot)
        line10.remove(line.blue_blood)
    if choice9 == line.cave_shoulders:
        line10.remove(line.delicate_skin)
        line10.remove(line.blue_blood)
        line10.remove(line.burnt_gold)
        line10.remove(line.spiderwebs)
    if choice9 == line.ribs or choice9 == line.ribs_edit:
        line10.remove(line.soot)
        line10.remove(line.blue_blood)
        line10.remove(line.spiderwebs)
    if choice9 == line.impress:
        line10.clear()
        line10.append(line.burnt_gold)
        line10.append(line.spiderwebs_edit)
    if choice9 == line.vanity:
        line10.remove(line.blue_blood)
        line10.remove(line.burnt_gold)
        line10.remove(line.spiderwebs)

    choice10 = f.get_choice(line10)
    if choice10 == line.blood_on_lips or choice10 == line.teeth_brush:
        line11.remove(line.acid_reeling)
        line11.remove(line.soldier)
        line11.remove(line.threat_of_pain)
        line11.remove(line.stay_trapped)
    if choice10 == line.soot:
        line11.remove(line.blunt_calloused)
    if choice10 == line.blue_blood:
        line11.remove(line.acid_reeling)
    if choice10 == line.gates:
        line11.remove(line.exuberant)

    choice11 = f.get_choice(line11)
    if choice11 == line.sharp_needle:
        line12.remove(line.dissipates)
    if choice11 == line.blunt_calloused:
        line12.remove(line.burn_uneasily)
        line12.remove(line.dissipates)
        line12.remove(line.sugar)
    if choice11 == line.exuberant:
        line12.remove(line.dissipates)
    if choice11 == line.acid_reeling:
        line12.clear()
        line12.append(line.teeth_bleeds)
        line12.append(line.fallen_loose)
    if choice11 == line.soldier:
        line12.clear()
        line12.append(line.blight_sun)
        line12.append(line.broken_you)
        line12.append(line.moments)
    if choice11 == line.threat_of_pain:
        line12.remove(line.burn_uneasily)
        line12.remove(line.blight_sun)
        line12.remove(line.broken_you)
        line12.remove(line.moments)
        line12.remove(line.sugar)
        line12.append(line.sugar_edit)
    if choice11 == line.stay_trapped:
        line12.remove(line.burn_uneasily)
        line12.append(line.fallen_loose)
        line12.append(line.dissipates)
    if choice11 == line.memory_of_corpse:
        line12.remove(line.burn_uneasily)
        line12.remove(line.dissipates)
        line12.remove(line.sugar)

    choice12 = f.get_choice(line12)

    f.poem_draft = False

    f.screen.fill(f.background_color)
    f.display_intro()
    f.display_poem()

    with open('Poem ' + str(loop_count) + '.txt', "w") as file:
        for item in f.user_poem:
            file.write(item)
            file.write('\n')
    file.close()

    quit_poem = False

    while not quit_poem:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                mainloop = False
                quit_poem = True
            if event.type == pygame.MOUSEBUTTONUP:
                f.user_poem.clear()
                f.counter.clear()
                f.counter.append(1)
                f.poem_draft = True
                loop_count += 1
                f.screen.fill(f.background_color)
                f.display_poem()
                f.display_intro()
                quit_poem = True
