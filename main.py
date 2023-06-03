from justpy import *


myopendialog = """
<div class="q-pa-md">

 <q-btn label="Prompt" color="primary" name="mybutton"/>

    <q-dialog name="mydialog">
      <q-card>
        <q-card-section>
          <div class="text-h6">Youtube Alert TEST</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum repellendus sit voluptate voluptas eveniet porro. Rerum blanditiis perferendis totam, ea at omnis vel numquam exercitationem aut, natus minima, porro labore.
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="OK" color="primary" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
</div>


"""

# AND NOW I WILL CREATE BOTTOM DIALOG

mybottomdialog = """
<div class="q-pa-md">
<q-btn label="Left" icon="keyboard_arrow_left" color="primary"

	name="mybuttonbottom"/>

    <q-dialog name="dialogbottom" position="bottom">
      <q-card style="width: 350px">
        <q-linear-progress value="0.6" color="pink" />

        <q-card-section class="row items-center no-wrap">
          <div>
            <div class="text-weight-bold">The Walker</div>
            <div class="text-grey">Fitz & The Tantrums</div>
          </div>

          <q-space />

          <q-btn flat round icon="fast_rewind" />
          <q-btn flat round icon="pause" />
          <q-btn flat round icon="fast_forward" />
        </q-card-section>
      </q-card>
    </q-dialog>


</div>
"""


def myapp():
	app = QuasarPage()

	def opendialog(self,msg):
		self.dialog.value = True


	# NOW I WILL COPY PASTE FROM QUASAR DIALOG
	my = parse_html(myopendialog,a=app)
	my.name_dict['mybutton'].dialog = my.name_dict['mydialog']
	# NOW IF YOU CLICK BUTTON THEN OPEN DIALOG
	my.name_dict['mybutton'].on("click",opendialog)


	# FOR DIALOG BOTTOM HERE
	bt = parse_html(mybottomdialog,a=app)
	bt.name_dict['mybuttonbottom'].dialog = bt.name_dict['dialogbottom']
	# NOW IF YOU CLICK BUTTON THEN OPEN DIALOG
	bt.name_dict['mybuttonbottom'].on("click",opendialog)




	return app

justpy(myapp)
