

print("settings ....")
game = input("enter game name: ")
print(" write color code or 'default' for each property")


with open('%s.css'%game, 'w+') as f:
  color1 = input("enter action bar color: ")
  color3 = input("enter text background color: ")
  color2 = input("enter button color:")
  color4 = input("enter text color:")
  color5 = input("enter text_links color:") 
  f.write('#app-%s .popover-content {    background: %s; }\n'%(game,color1))
  f.write ('#app-%s .contact-button {    background: %s;}\n'%(game,color2))
  f.write('#app-%s .contact-button:hover {    background: %s;}\n'%(game,color2))
  f.write('#app-%s .actions-wrapper{ background:  %s; border: 0px solid %s; }\n'%(game,color1, color1))
  f.write('#app-%s .section-title { background:  %s;border-top: 2px solid %s; }\n'%(game, color1, color1))
  f.write('#app-%s .faq-list { background:%s; border: 5px solid %s; }\n'%(game, color3,color1))
  f.write('#app-%s .faq-list a { color: %s;}\n\n'%(game,color5))
  f.write('#app-%s .answer-wrapper { background:  %s;border: 5px solid %s;padding: 0px;}\n'%(game,color3,color1))
  f.write('#app-%s .answer-wrapper a { color: %s;}\n\n'%(game,color5))
  f.write('#app-%s .answer-title { background:  %s; border-top: 2px solid %s;padding: 10px;}\n '%(game, color1, color1))
  f.write('#app-%s .answer-title  {  color: #ffffff !important;}\n'%game)
  f.write('#app-%s .answer {padding:30px;}\n'%game)
  f.write('#app-%s .breadcrumb { border-radius: 7px;  background:  %s; border-bottom: 1px solid %s; padding: 20px; color: white;}\n'%(game, color1, color1))
  f.write('#app-%s .breadcrumb .separator{color: white;}\n'%game)
  f.write('#app-%s .or-separator {    color: white;}\n'%game)
  f.write('#app-%s .mobile-nav { background: %s;}\n'%(game,color1))
  f.write('#app-%s .mobile-nav .popover-content-wrapper .label{ color: #fff; }\n'%game)

print("generating css")