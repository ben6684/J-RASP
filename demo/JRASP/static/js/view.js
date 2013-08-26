function add_good_comment(id_fb)
{
	/*$('good_comment_'+id).innerHTML = id*/
	new Ajax.Updater('good_comment_'+id_fb, "/article/add_comment/", {method:'get',parameters:{id_fb:id_fb} })
}
